from omieapi import Omie
import datetime

def get_active_pdv_products(omie_app):
    """Busca produtos ativos no PDV"""
    products = []
    page = 1
    while True:
        response = omie_app.listar_produtos(
            pagina=page,
            registros_por_pagina=50,
            filtrar_apenas_omiepdv="S",
            filtrar_apenas_pdv="S",
            inativo="N"
            # Filtra apenas produtos do PDV
        )
        
        if 'produto_servico_cadastro' in response:
            products.extend(response['produto_servico_cadastro'])
        
        total_pages = response.get('total_de_paginas', 1)
        if page >= total_pages:
            break
        page += 1
    
    # Filtra apenas produtos ativos
    lista_filtro_tipo_item = ['04', '05']
    active_products = [
        p for p in products 
        if not p.get('tipoItem') in lista_filtro_tipo_item
    ]
    return active_products

def get_stock_locations(omie_app):
    """Lista os locais de estoque disponíveis"""
    response = omie_app.listar_locais_estoque(**{
            "nPagina": 1,
            "nRegPorPagina": 50
        }
    )
    return response.get('locaisEncontrados', [])

def perform_stock_adjustment(omie_app, product_id, location_id, quantity, cost, date, notes="Ajuste via script"):
    """Realiza o ajuste de estoque para um produto"""
    adjustment = {
        "codigo_local_estoque": location_id,
        "id_prod": product_id,
        "data": date,
        "quan": quantity,
        "valor": cost,
        "obs": notes,
        "origem": "AJU",  # Ajuste manual
        "tipo": "SLD",    # Saldo
        "motivo": "INV"   # Inventário
    }
    
    response = omie_app._chamar_api(
        endpoint='estoque/ajuste/',
        method='IncluirAjusteEstoque',
        params=adjustment
    )
    return response

def main():
    # Configuração inicial
    APP_KEY = input("sua_app_key: ")      # Substitua pela sua chave
    APP_SECRET = input("seu_app_secret: ")  # Substitua pelo seu secret
    
    # Inicializa a API com sessão para melhor desempenho
    omie_app = Omie(APP_KEY, APP_SECRET, session=True)
    
    try:
        # Busca produtos ativos do PDV
        print("Buscando produtos ativos do PDV...")
        products = get_active_pdv_products(omie_app)
        if not products:
            print("Nenhum produto ativo encontrado no PDV.")
            return
        
        # Lista locais de estoque
        locations = get_stock_locations(omie_app)
        if not locations:
            print("Nenhum local de estoque encontrado.")
            return
        
        # Mostra locais de estoque disponíveis
        print("\nLocais de estoque disponíveis:")
        for i, loc in enumerate(locations):
            print(f"{i+1}. {loc['descricao']} (Código: {loc['codigo']})")
        
        # Solicita input do usuário
        location_choice = int(input("\nEscolha o número do local de estoque: ")) - 1
        if location_choice < 0 or location_choice >= len(locations):
            print("Local inválido!")
            return
        
        location_id = locations[location_choice]['codigo_local_estoque']
        
        date = input("Digite a data do ajuste (DD/MM/AAAA) ou pressione Enter para hoje: ")
        if not date:
            date = datetime.datetime.now().strftime("%d/%m/%Y")
        else:
            # Validação simples da data
            try:
                datetime.datetime.strptime(date, "%d/%m/%Y")
            except ValueError:
                print("Formato de data inválido! Use DD/MM/AAAA")
                return
        
        # Loop pelos produtos
        print("\nProdutos encontrados:")
        for i, product in enumerate(products):
            print(f"{i+1}. {product['descricao']} (ID: {product['codigo_produto']})")
        
        print("\nAjuste de estoque - Digite 0 para pular um produto")
        for product in products:
            print(f"\nProduto: {product['descricao']}")
            
            quantity = input("Quantidade (ex: 10 ou 10.5): ")
            if quantity == "0":
                print("Produto pulado.")
                continue
                
            try:
                quantity = float(quantity)
                if quantity < 0:
                    raise ValueError("Quantidade não pode ser negativa")
            except ValueError:
                print("Quantidade inválida! Produto pulado.")
                continue
                
            cost = input("Custo unitário (ex: 25.99): ")
            try:
                cost = float(cost)
                if cost < 0:
                    raise ValueError("Custo não pode ser negativo")
            except ValueError:
                print("Custo inválido! Produto pulado.")
                continue
            
            # Realiza o ajuste
            response = perform_stock_adjustment(
                omie_app,
                product['codigo_produto'],
                location_id,
                quantity,
                cost,
                date
            )
            
            if 'codigo_status' in response and response['codigo_status'] == '0':
                print("Ajuste realizado com sucesso!")
            else:
                print(f"Erro no ajuste: {response.get('descricao_status', 'Erro desconhecido')}")
                
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
    
    finally:
        # Fecha a sessão
        omie_app.fechar_session()

if __name__ == "__main__":
    main()