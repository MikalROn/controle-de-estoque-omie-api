# Micro sistema para Ajuste do estoque

Eu preciso de um pequeno sistema que integra com a api omie, busque os produtos que são vendios no pdv  e estão ativos,
faça um loop entre eles e faça um ajuste no estoque.

# Dependencias e ferramentas

- Python 
- Omie Api (Biblioteca que irei te mandar a da documentação)

Caso necessário adicione outra biblioteca


# Pontos importantes

O sistema deve funcionar no terminal, ele obrigatoriamente tem q aceitar meus inputs, como data, etc, deve conter a escolha do local do estoque,a data e o local de estoque deve ser o mesmo para todos os produtos , ele deve pedir qunatidade custo do produto

# Documentação
<documentacao-omie>Home Lista de API's
Veja abaixo a lista dos módulos/serviços que estão disponíveis para consumo via a API. Consulte a documentação e faça testes online clicando em cada um deles.

Geral
Alguns cadastros no Omie são compartilhados por todos os módulos, como por exemplo clientes e fornecedores

Clientes, Fornecedores, Transportadoras, etc	Cria/edita/consulta o cadastro de clientes, fornecedores, transportadoras, etc	v1
Clientes - Características	Cria/edita/consulta características de clientes	v1
Tags	Cria/edita/consulta tags quem são usadas no cadastro de clientes, fornecedores, etc	v1
Projetos	Cria/edita/consulta projetos	v1
Cadastros Auxiliares
Empresas	Lista o cadastro da empresa	v1
Departamentos	Lista o cadastro de departamentos	v1
Categorias	Lista o cadastro de categorias	v1
Parcelas	Lista as parcelas cadastradas	v1
Tipos de Atividade da Empresa	Lista os tipos de atividade da empresa	v1
CNAE		v1
Cidades	Lista o cadastro de cidades	v1
Países	Lista o cadastro de países	v1
Tipos de Anexos	Consulta Tipos de Anexos	v1
Documentos Anexos	Criar/edita/consulta e exclui documentos anexos	v1
Tipo de Entrega	Criar/edita/consulta e exclui tipo de entrega de fornecedores	v1
Tipo de Assinante	Lista os Tipos de Assinante	v1
CRM
Contas + Contatos + Oportunidades para fechar mais negócios e vender mais

Contas	Cria/edita/consulta Contas	v1
Contas - Características	Cria/edita/consulta caracterísitcas da conta	v1
Contatos	Cria/edita/consulta Contatos	v1
Oportunidades	Cria/edita/consulta Oportunidades	v1
Oportunidades - Resumo	Resumo de Oportunidades	v1
Tarefas	Cria/edita/consulta Tarefas	v1
Tarefas - Resumo	Resumo de Tarefas	v1
Cadastros Auxiliares
Soluções	Lista das soluções ofertadas através do CRM	v1
Fases	Lista as fases da oportunidade	v1
Usuários	Lista dos usuários do CRM	v1
Status	Lista status possíveis de uma oportunidade	v1
Motivos	Lista motivos de conclusão de uma oportunidade	v1
Tipos	Lista os tipos disponíveis de uma oportunidade	v1
Parceiros	Lista dos parceiros e equipes	v1
Finders	Lista dos finders cadastrados	v1
Origens	Lista de origens disponíveis para a oportunidade	v1
Concorrentes	Lista dos concorrentes cadastrados	v1
Verticais	Lista das verticais atendidas	v1
Vendedores	Lista dos vendedores ativos no CRM	v1
Telemarketing	Lista dos atendentes de telemarketing	v1
Pré-Vendas	Lista dos usuários de pré-venda	v1
Tipos de Tarefas	Criar/edita/consulta e exclui Tipos de Tarefas	v1
Finanças
Extrato multi-contas + Contas a Receber + Contas a Pagar + Fluxo de Caixa

Contas Correntes	Cria/edita/consulta o cadastro de contas correntes	v1
Contas Correntes - Lançamentos	Cria/edita/consulta lançamentos na conta corrente	v1
Contas a Pagar - Lançamentos	Cria/edita/consulta títulos a pagar	v1
Contas a Receber - Lançamentos	Cria/edita/consulta títulos a receber	v1
Contas a Receber - Boletos	Gera/Obtém/Prorroga e Cancela Boletos de um título a receber	v1
Contas a Receber - PIX	Gera um PIX para um contas a receber do Omie.CASH	v1
Extrato de Conta Corrente	Listagem do extrato de conta corrente	v1
Orçamento de Caixa	Listagem do orçamento de caixa (Previsto x Realizado)	v1
Pesquisar Títulos	Lista de títulos a pagar e receber	v1
Movimentos Financeiros	Consulta de pagamentos, baixas, lançamentos no Conta Corrente.	v1
Resumo	Resumo de Finanças	v1
Cadastros Auxiliares
Bancos	Lista o cadastro de instituições bancárias	v1
Tipos de Documento	Lista os tipos de documentos	v1
Tipos de Contas Correntes	Lista os tipos de contas correntes	v1
Contas do DRE	Lista as Contas do DRE	v1
Finalidade de Transferência	Lista as Finalidades de Transferência do CNAB	v1
Origem do títulos	Lista as origens dos títulos	v1
Bandeiras de Cartão	Lista as Bandeiras de Cartão de débito e crédito	v1
Compras, Estoque e Produção
Gerencie suas compras, estoque e ordens de produção

Produtos	Cria/edita/consulta produtos	v1
Produtos - Características	Cria/edita/consulta características de um determinado produto	v1
Produtos - Estrutura	Consulta estrutura de um determinado produto	v1
Produtos - Kit	Edita kit de produtos	v1
Requisições de Compra	Cria/edita/consulta requisições de compra	v1
Pedidos de Compra	Cria/edita/consulta pedidos de compra	v1
Ordens de Produção	Cria/edita/consulta ordens de produção	v1
Nota de Entrada	Cria/EditaConsulta Notas de Entrada	v1
Nota de Entrada - Faturamento	Operações de faturamento de Notas de Entrada	v1
Recebimento de Nota Fiscal	Edita os dados do Recebimento de uma NF-e	v1
Resumo	Resumo de compras	v1
Cadastros Auxiliares
Familias de Produto	Cria/edita/consulta famílias de produto	v1
Unidades	Consulta unidades de medida	v1
Compradores	Consulta lista de compradores cadastrados	v1
Produto x Fornecedor	Lista relação entre produtos e fornecedores	v1
Formas de Pagamento	Lista as opções de forma de pagamento de uma compra	v1
NCM	Lista/consulta de códigos NCM (Nomenclatura Comum do Mercosul)	v1
Cenário de Impostos	Lista os Cenários de Impostos	v1
Impostos
CFOP		v1
CNAE		v1
ICMS - CST		v1
ICMS - CSOSN		v1
ICMS - Origem da Mercadoria		v1
PIS - CST		v1
COFINS - CST		v1
IPI - CST		v1
IPI - Enquadramento		v1
Tipo de Cálculo		v1
CEST		v1
Estoque
Ajustes de Estoque	Cria/exclui movimentações do estoque	v1
Consulta Estoque	Consulta consolidada do estoque do produto	v1
Movimento Estoque	Lista os movimentos de estoque de entrada/saida por período	v1
Locais de Estoque	Listagem dos Locais de Estoque	v1
Resumo do Estoque	Resumo do Estoque de um produto	v1
Vendas e NF-e
Venda + Faturamento + Emissão de NF-e

Pedidos de Venda
Pedidos de Venda - Resumido	Adiciona pedidos e itens de venda de produto	v1
Pedidos de Venda	Cria/edita/consulta pedidos e orçamentos	v1
Pedidos de Venda - Faturamento	Operações de faturamento de pedido	v1
Pedidos de Venda - Etapas	Consulta das etapas de pedido	v1
CT-e / CT-e OS	Adiciona/Cancela Conhecimento de Transporte	v1
Remessa de Produtos	Cria/edita uma NF de remessa de produto	v1
Remessa de Produtos - Faturamento	Operações de faturamento da Remessa	v1
Resumo	Resumo de vendas de NF-e, CT-e e Cupom Fiscal	v1
Obter Documentos	Disponibiliza PDF e XML de documentos fiscais (NF-e, NFC-e, CT-e, etc)	v1
Produtos
Produtos	Cria/edita/consulta produtos	v1
Produtos - Características	Cria/edita/consulta características de um determinado produto	v1
Produtos - Kit	Edita kit de produtos	v1
Cupom Fiscal
Adicionar	Adicionar cupom fiscal/NFC-e/CF-e SAT	v1
Cancelar ou excluir	Cancelar/excluir/inutilizar cupons fiscais	v1
Consultar	Consultas de Cupom Fiscal	v1
Importar NFC-e	Importação de XML de NFC-e	v1
Importar CFe-Sat	Importação de XML de CFe-Sat	v1
Cadastros Auxiliares
Vendedores	Cria/edita/consulta o cadastro de vendedores	v1
Formas de Pagamento	Lista as formas de pagamento de um pedido de venda	v1
Tabela de Preços	Cria/edita/consulta tabelas de preço usadas no pedido de venda	v1
Características de produtos	Cria/edita/consulta características que serão usadas nos produtos	v1
NCM	Lista/consulta de códigos NCM (Nomenclatura Comum do Mercosul)	v1
Etapas de Faturamento	Lista as etapas do faturamento	v1
Cenário de Impostos	Lista os Cenários de Impostos	v1
Meios de Pagamento	Listagem de meios de pagamentos (parcelas)	v1
Origem do Pedido	Lista as origens de pedidos disponíveis	v1
Motivos de Devolução	Lista os Motivos de Devolução	v1
NF-e
Consultas	Lista de NF-e emitidas	v1
Utilitários	Recupera URL da NF-e (XML), do Danfe ou do logotipo da empresa	v1
Importar	Importação de XML de NF-e	v1
Serviços e NFS-e
Ordens de Serviço + Contratos + Faturamento + Emissão de NFS-e

Serviços	Cria/edita/consulta serviços prestados pela empresa	v1
Ordens de Serviço	Cria/edita/consulta uma ordem de serviço	v1
Ordens de Serviço - Faturamento	Operações de faturamento de OS	v1
Ordens de Serviço - Fat. em Lote	Faturamento de Ordens de Serviço em Lote	v1
Contratos de Serviço	Cria/edita/consulta contratos de serviço (recorrência)	v1
Contratos de Serviço - Faturamento	Operações de faturamento do Contrato de Serviço	v1
Contratos de Serviço - Fat. em Lote	Faturamento de Contratos de Serviço em Lote	v1
Resumo	Resumo do Faturamento de Serviços	v1
Obter Documentos	Disponibiliza PDF e XML de documentos fiscais (NFS-e, Recibo, Via Única, etc)	v1
NFS-e
Consultas	Listagem de NFS-e emitidas	v1
Cadastros Auxiliares
Vendedores	Cria/edita/consulta o cadastro de vendedores	v1
Serviços no Município	Lista serviços disponíveis para o município	v1
Tipos de Tributação	Lista os tipos de tributação	v1
LC 116	Lista os códigos da Lei Complementar 116	v1
NBS	Lista os códigos de Nomenclatura Brasileira Serviços (NBS)	v1
IBPT	Lista de impostos definidos na tabela do IBPT	v1
Formas de Pagamento	Lista as formas de pagamento	v1
Tipo de Faturamento de Contrato	Lista os tipos de faturamento de contratos	v1
Etapas de Faturamento	Lista as etapas do faturamento	v1
Tipo de utilização	Lista os Tipos de utilização	v1
Classificação do Serviço	Lista as Classificações do Serviço	v1
Painel do Contador
Integrações que fazem parte do escritório contábil :)

Documentos Fiscais	Listagem dos XMLs de Documentos Fiscais (NF-e/NFC-e/CF-e SAT/NFS-e)	v1
Resumo	Resumo do Fechamento Contábil	v1

LocalEstoque
Endpoint
WSDL
PHP SOAP
JSON
Endpoint URI
https://app.omie.com.br/api/v1/estoque/local/
Métodos
Veja abaixo a documentação de cada método disponí­vel para este serviço.

AlterarLocalEstoque
Alterar local de Estoque

Parâmetros:
 	alterarLocalRequest	alterarLocalRequest	
Requisição para alteração do Local de Estoque cadastrado.
Retorno alterarLocalResponse:
Exemplo:
{
  "codigo": "L0",
  "descricao": "descrição de teste",
  "tipo": "1",
  "dispOrdemProducao": "N",
  "codigo_cliente": 0,
  "dispConsumoOP": "N",
  "dispRemessa": "N",
  "dispVenda": "N"
}
IncluirLocalEstoque
Adiciona um local de estoque

Parâmetros:
 	IncluirLocalRequest	IncluirLocalRequest	
Solicitação de inclusão de Local de Estoque.
Retorno incluirLocalResponse:
Exemplo:
{
  "codigo": "L0",
  "descricao": "descrição de teste",
  "tipo": "1",
  "dispOrdemProducao": "N",
  "dispConsumoOP": "N",
  "dispRemessa": "N",
  "dispVenda": "N",
  "consiSugeCompra": "N"
}
ListarLocaisEstoque
Lista os Locais de Estoque encontrados.

Parâmetros:
 	locaisListarRequest	locaisListarRequest	
Solicitação de listagem de Locais de Estoque.
Retorno locaisListarResponse:
Exemplo:
{
  "nPagina": 1,
  "nRegPorPagina": 20
}
Tipos Complexos
IncluirLocalRequest
codigo	string50	Código do Local do Estoque.+
descricao	string250	Descrição do Local de Estoque.
tipo	string1	Tipo de Local de Estoque.+
consiSugeCompra	string1	Indica se o Local de Estoque deve ser considerado na sugestão de compra
codigo_cliente	integer	Código do cliente/fornecedor.
dispOrdemProducao	string1	Indica se o Local do Estoque está disponível para Ordem de Produção (S/N).
dispConsumoOP	string1	Indica se o Local do Estoque está disponível para consumo da Ordem de Produção (S/N).
dispRemessa	string1	Indica se o Local do Estoque está disponível para Remessa (S/N).
dispVenda	string1	Indica se o Local do Estoque está disponível para Venda (S/N).
alterarLocalRequest
codigo_local_estoque	integer	Código do Local do Estoque.+
codigo	string50	Código do Local do Estoque.+
descricao	string250	Descrição do Local de Estoque.
tipo	string1	Tipo de Local de Estoque.+
consiSugeCompra	string1	Indica se o Local de Estoque deve ser considerado na sugestão de compra
codigo_cliente	integer	Código do cliente/fornecedor.
dispOrdemProducao	string1	Indica se o Local do Estoque está disponível para Ordem de Produção (S/N).
dispConsumoOP	string1	Indica se o Local do Estoque está disponível para consumo da Ordem de Produção (S/N).
dispRemessa	string1	Indica se o Local do Estoque está disponível para Remessa (S/N).
dispVenda	string1	Indica se o Local do Estoque está disponível para Venda (S/N).
alterarLocalResponse
codigo_local_estoque	integer	Código do Local do Estoque.+
cCodStatus	string4	Codigo de Status
cDesStatus	text	Descricao do Status
incluirLocalResponse
codigo_local_estoque	integer	Código do Local do Estoque.+
codigo	string50	Código do Local do Estoque.+
cCodStatus	string4	Codigo de Status
cDesStatus	text	Descricao do Status
locaisEncontrados
Lista de Locais de Estoque encontrados.

codigo_local_estoque	integer	Código do Local do Estoque.+
codigo	string50	Código do Local do Estoque.+
descricao	string250	Descrição do Local de Estoque.
tipo	string1	Tipo de Local de Estoque.+
padrao	string1	Indica se o Local do Estoque é padrão (S/N).
inativo	string1	Indica se o Local do Estoque está inativo (S/N).
codigo_cliente	integer	Código do cliente/fornecedor.
dispOrdemProducao	string1	Indica se o Local do Estoque está disponível para Ordem de Produção (S/N).
dispConsumoOP	string1	Indica se o Local do Estoque está disponível para consumo da Ordem de Produção (S/N).
dispRemessa	string1	Indica se o Local do Estoque está disponível para Remessa (S/N).
dispVenda	string1	Indica se o Local do Estoque está disponível para Venda (S/N).
dInc	text	Data de Inclusão.
hInc	string8	Hora de inclusão.
uInc	string10	Código do usuário que realizou a inclusão.
dAlt	string8	Hora de alteração.
hAlt	string8	Hora de alteração.
uAlt	string10	Código do usuário que realizou a alteração.
locaisEncontradosArray
Este parâmetro é um array do tipo locaisEncontrados

Lista de locaisEncontrados

locaisListarRequest
nPagina	integer	Número da página que será listada.
nRegPorPagina	integer	Número de registros retornados
filtrar_por_data_de	string10	Filtrar os registros a partir de uma data.+
filtrar_por_hora_de	string8	Filtrar a partir da hora.+
filtrar_por_data_ate	string10	Filtrar os registros até uma data.+
filtrar_por_hora_ate	string8	Filtrar até a hora.+
filtrar_apenas_inclusao	string1	Filtrar apenas os registros incluídos (S/N).+
filtrar_apenas_alteracao	string1	Filtrar apenas os registros alterados (S/N).+
locaisListarResponse
nPagina	integer	Número da página que será listada.
nTotPaginas	integer	Total de páginas encontradas.
nRegistros	integer	Número de registros retornados
nTotRegistros	integer	Total de registros encontrados.
locaisEncontrados	locaisEncontradosArray	Lista de Locais de Estoque encontrados.
omie_fail
code	integer	Codigo do erro
description	text	Descricao do erro
referer	text	Origem do erro
fatal	boolean	Indica se eh um erro fatal

AjusteEstoque
Endpoint
WSDL
PHP SOAP
JSON
Endpoint URI
https://app.omie.com.br/api/v1/estoque/ajuste/
Métodos
Veja abaixo a documentação de cada método disponí­vel para este serviço.

AlterarEstoqueMinimo

Parâmetros:
 	estoque_mov_ajuste_estoque_minimo	estoque_mov_ajuste_estoque_minimo	
Registro do movimento de ajuste de estoque mínimo
Retorno estoque_mov_ajuste_estoque_minimo_resposta:
Exemplo:
{
  "codigo_local_estoque": 0,
  "id_prod": 16487740,
  "cod_int": "",
  "quan_min": "15"
}
ExcluirAjusteEstoque
Excluir um Movimento de Ajuste de Estoque

Parâmetros:
 	estoque_mov_ajuste_cadastro_id_ajuste	estoque_mov_ajuste_cadastro_id_ajuste	
ID do Registro do Ajuste de Estoque
Retorno estoque_mov_ajuste_cadastro_resposta: Status de Resposta para o Ajuste de Estoque
Exemplo:
{
  "id_ajuste": 0
}
IncluirAjusteEstoque
Incluir um Ajuste de Estoque

Parâmetros:
 	estoque_mov_ajuste_cadastro	estoque_mov_ajuste_cadastro	
Registro do Movimento de Ajuste de Estoque
Retorno estoque_mov_ajuste_cadastro_resposta: Status de Resposta para o Ajuste de Estoque
Exemplo:
{
  "codigo_local_estoque": 0,
  "id_prod": 16487740,
  "data": "24/02/2025",
  "quan": "15",
  "obs": "Ajuste feito pela ferramenta de Teste de API (23710)",
  "origem": "AJU",
  "tipo": "SLD",
  "motivo": "INV",
  "valor": 10
}
ListarAjusteEstoque
Listar os ajuste de estoque.

Parâmetros:
 	estoque_mov_listar_request	estoque_mov_listar_request	
Solicitação de listagem de ajuste de estoque.
Retorno estoque_mov_listar_response:
Exemplo:
{
  "pagina": 1,
  "registros_por_pagina": 100,
  "apenas_importado_api": "N"
}
Tipos Complexos
ajuste_estoque_lista
id_ajuste	integer	Código do local do estoque.
cod_int_ajuste	string60	Código de Integração com sistemas legados.
codigo_local_estoque	integer	Código do local do estoque.
id_prod	integer	Código do produto.
data	string10	Data do ajuste.
obs	text	Observação do movimento de estoque.
codigo_local_estoque_ds	integer	ID do Local de Estoque de Destino
quan	decimal	quantidade do movimento.
valor	decimal	Valor do Movimento.
tipo	string3	Tipo do Ajuste de Estoque.+
origem	string3	Origem do Movimento de Estoque.+
motivo	string3	Motivo do ajuste.+
bloqueado	string1	Cadastro Bloqueado pela API [S/N]
imp_api	string1	Gerado pela API [S/N]
ajuste_estoque_listaArray
Este parâmetro é um array do tipo ajuste_estoque_lista

Lista de ajuste_estoque_lista

estoque_mov_ajuste_cadastro
Registro do Movimento de Ajuste de Estoque

codigo_local_estoque	integer	Código do local do estoque.+
id_prod	integer	Código do produto.
cod_int	string20	Código de Integração do Produto.+
cod_int_ajuste	string60	Código de Integração com sistemas legados.
data	string10	Data do Movimento.+
tipo	text	Tipo do Ajuste de Estoque.+
quan	decimal	Novo valor para quantidade mínima no estoque.+
valor	decimal	Valor do Movimento.+
obs	text	Observação do Movimento de Estoque.+
origem	string3	Origem do Movimento de Estoque.+
motivo	string3	Motivo do ajuste.+
codigo_local_estoque_destino	integer	Obrigatório quando utilizar Tipo = "TRF"+
empresa	integer	Código da empresa. +
estoque_mov_ajuste_cadastro_id_ajuste
ID do Registro do Ajuste de Estoque

id_ajuste	integer	ID do Movimento de Ajuste de Estoque
estoque_mov_ajuste_cadastro_resposta
Status de Resposta para o Ajuste de Estoque

codigo_status	text	Código do status de resposta do ajuste de estoque mínimo
descricao_status	text	Descrição do status de resposta do ajuste de estoque mínimo
id_movest	integer	ID do Movimento de Ajuste de Estoque (Original)
id_ajuste	integer	ID do Movimento de Ajuste de Estoque
estoque_mov_ajuste_estoque_minimo
codigo_local_estoque	integer	Código do local do estoque.+
cod_int	string20	Código de Integração do Produto.+
id_prod	integer	Código do produto.
quan_min	decimal	Novo valor para quantidade mínima no estoque.+
estoque_mov_ajuste_estoque_minimo_resposta
codigo_status	text	Código do status de resposta do ajuste de estoque mínimo
descricao_status	text	Descrição do status de resposta do ajuste de estoque mínimo
estoque_mov_listar_request
pagina	integer	Número da página que será listada.
registros_por_pagina	integer	Número de registros retornados
ordenar_por	string100	Ordenar o resultado da página por:+
cod_int_ajuste	string60	Código de Integração com sistemas legados.
codigo_local_estoque	integer	Código do local do estoque.
id_prod	integer	Código do Produto.
tipo	string3	Tipo do Ajuste de Estoque.+
origem	string3	Origem do Movimento de Estoque.+
motivo	string3	Motivo do ajuste.+
data_movimento_de	string10	Data do Movimento inicio.
data_movimento_ate	string10	Data movimento final.
apenas_importado_api	string1	Preencher com "S" ou "N".
estoque_mov_listar_response
pagina	integer	Número da página que será listada.
total_de_paginas	integer	Total de páginas encontradas.
registros	integer	Número de registros retornados
total_de_registros	integer	Total de registros encontrados.
ajuste_estoque_lista	ajuste_estoque_listaArray	Estoque mínimo para o produto.
omie_fail
code	integer	Codigo do erro
description	text	Descricao do erro
referer	text	Origem do erro
fatal	boolean	Indica se eh um erro fatal

ProdutosCadastro
Endpoint
WSDL
PHP SOAP
JSON
Endpoint URI
https://app.omie.com.br/api/v1/geral/produtos/
Métodos
Veja abaixo a documentação de cada método disponí­vel para este serviço.

AlterarProduto

Parâmetros:
 	produto_servico_cadastro	produto_servico_cadastro	
Cadastro completo de produtos
Retorno produto_servico_status: Status de retorno do cadastro de produtos
Exemplo:
{
  "codigo_produto_integracao": "1740419652",
  "codigo": "teste0001",
  "descricao": "Produto de teste",
  "unidade": "UN"
}
AssociarCodIntProduto

Parâmetros:
 	produto_servico_cadastro_chave	produto_servico_cadastro_chave	
Pesquisa de produtos
Retorno produto_servico_status: Status de retorno do cadastro de produtos
Exemplo:
{
  "codigo_produto": 0,
  "codigo_produto_integracao": ""
}
ConsultarProduto
Consulta um produto.

Parâmetros:
 	produto_servico_cadastro_chave	produto_servico_cadastro_chave	
Pesquisa de produtos
Retorno produto_servico_cadastro: Cadastro completo de produtos
Exemplo:
{
  "codigo_produto": 0,
  "codigo_produto_integracao": "",
  "codigo": ""
}
ExcluirProduto
Exclui um produto

Parâmetros:
 	produto_servico_cadastro_chave	produto_servico_cadastro_chave	
Pesquisa de produtos
Retorno produto_servico_status: Status de retorno do cadastro de produtos
Exemplo:
{
  "codigo_produto": 0,
  "codigo_produto_integracao": "",
  "codigo": ""
}
IncluirProduto
Incluir um produto.

Parâmetros:
 	produto_servico_cadastro	produto_servico_cadastro	
Cadastro completo de produtos
Retorno produto_servico_status: Status de retorno do cadastro de produtos
Exemplo:
{
  "codigo_produto_integracao": "1740419652",
  "codigo": "teste0001",
  "descricao": "Produto de teste",
  "unidade": "UN"
}
IncluirProdutosPorLote
DEPRECATED

Parâmetros:
 	produto_servico_lote_request	produto_servico_lote_request	
Importação em Lote de produtos
Retorno produto_servico_lote_response: Resposta do processamento do lote de produto importados.
Exemplo:
{
  "lote": 123,
  "produto_servico_cadastro": [
    {
      "codigo_produto_integracao": "1628097039",
      "codigo": "teste1235",
      "descricao": "Produto de teste",
      "unidade": "UN",
      "ncm": "9504.50.00"
    },
    {
      "codigo_produto_integracao": "1628097040",
      "codigo": "teste1234",
      "descricao": "Produto de teste",
      "unidade": "UN",
      "ncm": "9504.50.00"
    }
  ]
}
ListarProdutos
Lista completa do cadastro de produtos

Parâmetros:
 	produto_servico_list_request	produto_servico_list_request	
Lista os produtos cadastrados
Retorno produto_servico_listfull_response: Lista completa de produtos encontrados no omie.
Exemplo:
{
  "pagina": 1,
  "registros_por_pagina": 50,
  "apenas_importado_api": "N",
  "filtrar_apenas_omiepdv": "N"
}
ListarProdutosResumido
Lista os produtos cadastrados

Parâmetros:
 	produto_servico_list_request	produto_servico_list_request	
Lista os produtos cadastrados
Retorno produto_servico_list_response: Lista de produtos encontrados no omie.
Exemplo:
{
  "pagina": 1,
  "registros_por_pagina": 50,
  "apenas_importado_api": "N",
  "filtrar_apenas_omiepdv": "N"
}
UpsertProduto

Parâmetros:
 	produto_servico_cadastro	produto_servico_cadastro	
Cadastro completo de produtos
Retorno produto_servico_status: Status de retorno do cadastro de produtos
Exemplo:
{
  "codigo_produto_integracao": "1740419652",
  "codigo": "teste0001",
  "descricao": "Produto de teste",
  "unidade": "UN"
}
UpsertProdutosPorLote
DEPRECATED

Parâmetros:
 	produto_servico_lote_request	produto_servico_lote_request	
Importação em Lote de produtos
Retorno produto_servico_lote_response: Resposta do processamento do lote de produto importados.
Exemplo:
{
  "lote": 123,
  "produto_servico_cadastro": [
    {
      "codigo_produto_integracao": "1628097039",
      "codigo": "teste1235",
      "descricao": "Produto de teste 1235",
      "unidade": "UN",
      "ncm": "9504.50.00"
    },
    {
      "codigo_produto_integracao": "1628097040",
      "codigo": "teste1234",
      "descricao": "Produto de teste 1234",
      "unidade": "UN",
      "ncm": "9504.50.00"
    }
  ]
}
Tipos Complexos
armamento
Detalhamento especifco para cadastro de armamentos.

serie_cano	string15	Número de série do cano
descr_arma	string256	Descrição completa da arma
serie_arma	string15	Número de série da arma
tipo_arma	string1	Indicador do tipo de arma de fogo
caracteristicas
lista de caracteristicas do produto.

nCodCaract	integer	Código da característica de produto.+
cCodIntCaract	string20	Código de integração da característica do produto.+
cNomeCaract	string30	Nome da característica.
cConteudo	string60	Conteúdo da característica.
cExibirItemNF	string1	Exibir esta característica no item da NF-e emitida (S/N).
cExibirItemPedido	string1	Exibir esta característica no item do Pedido, Remessa ou Devolução (S/N).
cExibirOrdemProd	string1	Exibe esta característica na Ordem de Produção e Mapa de Custo (S/N).
caracteristicasArray
Este parâmetro é um array do tipo caracteristicas

Lista de caracteristicas

combustivel
codigo_anp	string9	Código de Produto da ANP.
descr_anp	string95	Descrição do Produto conforme ANP.
percent_glp	decimal	Percentual de GLP Derivado do Petróleo.
percent_gas_nac	decimal	Percentual de Gás Natural Nacional.
percent_gas_imp	decimal	Percentual de Gás Natural Importado.
valor_part	decimal	Valor de partida
componentes_kit
Componetes do KIT.

codigo_componente	integer	Identificação do componente do KIT, deve ser utilizado para Alterar e Excluir o componente.+
codigo_produto_componente	integer	Código do produto componente.+
quantidade_componente	decimal	Quantidade do componente.
valor_unitario_componente	decimal	Valor unitário do componente.
local_estoque_componente	integer	Local estoque do componente.
componentes_kitArray
Este parâmetro é um array do tipo componentes_kit

Lista de componentes_kit

dadosIbpt
Dados do IBPT.

aliqFederal	decimal	Carga tributária federal para os produtos nacionais.+
aliqEstadual	decimal	Carga tributária estadual.+
aliqMunicipal	decimal	Carga tributária municipal.+
fonte	string34	Fonte do IBPT.+
chave	string6	Número da versão do arquivo do IBPT.+
versao	string6	Versão da Tabela IBPT.+
valido_de	string10	Tabela do IBPT válilda a partir da data.+
valido_ate	string10	Tabela do IBPT valida até a data.+
imagens
Lista de imagens do produto.

url_imagem	text	URL da Imagem do produto.
imagensArray
Este parâmetro é um array do tipo imagens

Lista de imagens

info
dInc	string10	Data da Inclusão.+
hInc	string8	Hora da Inclusão.+
uInc	string10	Usuário da Inclusão.+
dAlt	string10	Data da Alteração.+
hAlt	string8	Hora da Alteração.+
uAlt	string10	Usuário da Alteração.+
cImpAPI	string1	Importado pela API (S/N).+
medicamento
cod_anvisa	string13	Código de produto Anvisa
preco_max_cons	decimal	Preço máximo consumidor
omie_fail
code	integer	Codigo do erro
description	text	Descricao do erro
referer	text	Origem do erro
fatal	boolean	Indica se eh um erro fatal
produto_servico_cadastro
Cadastro completo de produtos

codigo_produto	integer	Código do produto.+
codigo_produto_integracao	string60	Código de integração do produto.+
codigo	string60	Código do Produto.+
descricao	string120	Descrição do produto.+
unidade	string6	Código da Unidade.+
ncm	string13	Código da Nomenclatura Comum do Mercosul (NCM).+
ean	string14	Código EAN (GTIN - Global Trade Item Number).+
valor_unitario	decimal	Preço Unitário de Venda.+
codigo_familia	integer	Código da Familia do Produto.+
tipoItem	string2	Código do Tipo do Item para o SPED.+
recomendacoes_fiscais	recomendacoes_fiscais	Recomendações Fiscais.
peso_liq	decimal	Peso Líquido (Kg).+
peso_bruto	decimal	Peso Bruto (Kg).+
altura	decimal	Altura (centimentos).+
largura	decimal	Largura (centimetros)+
profundidade	decimal	Profundidade (centimetros).+
marca	string60	Marca.+
modelo	string60	Modelo.+
dias_garantia	integer	Dias de Garantia.+
dias_crossdocking	integer	Dias de Crossdocking.+
descr_detalhada	text	Descrição Detalhada para o Produto.+
obs_internas	text	Observações Internas.+
imagens	imagensArray	Lista de imagens do produto.
videos	videosArray	Lista de videos do produto.
caracteristicas	caracteristicasArray	lista de caracteristicas do produto.
tabelas_preco	tabelas_precoArray	Lista de tabelas de preço.
info	info	Informações complemetares do cadastro do produto.
exibir_descricao_nfe	string1	Indica se a Descrição Detalhada deve ser exibida nas Informações Adicionais do Item da NF-e (S/N).
exibir_descricao_pedido	string1	Indica se a Descrição Detalhada deve ser exibida na impressão do Pedido (S/N).
medicamento	medicamento	Detalhamento específico para cadastro de medicamentos+
combustivel	combustivel	Detalhamento específico para cadastro de combustíveis.+
veiculo	veiculo	Detalhamento específico para cadastro de veículos+
armamento	armamento	Detalhamento especifco para cadastro de armamentos.+
cst_icms	string2	Código da Situação Tributária do ICMS.+
modalidade_icms	string1	Modalidade da Base de Cálculo do ICMS.+
csosn_icms	string3	Código da Situação Tributária para Simples Nacional.+
aliquota_icms	decimal	Alíquota de ICMS.+
red_base_icms	decimal	Percentual de redução de base do ICMS.+
motivo_deson_icms	string2	Motivo da desoneração do ICMS.+
per_icms_fcp	decimal	Percentual do Fundo de Combate a Pobreza do ICMS.+
codigo_beneficio	string20	Código de integração da característica do produto.+
cst_pis	string2	Código da Situação Tributária do PIS.+
aliquota_pis	decimal	Alíquota do PIS.+
red_base_pis	decimal	Percentual de redução de base do PIS.+
cst_cofins	string2	Código da Situação Tributária do COFINS.+
aliquota_cofins	decimal	Alíquota do COFINS.+
red_base_cofins	decimal	Percentual de redução de base do COFINS.+
cfop	string10	CFOP do Produto.+
dadosIbpt	dadosIbpt	Dados do IBPT.+
codInt_familia	string20	Código de Integração da Familia do Produto.+
descricao_familia	string50	Descrição da Familia do Produto.+
bloqueado	string1	Indica se o registro está bloqueado (S/N).+
bloquear_exclusao	string1	Indica se a exclusão do registro está bloqueada (S/N).+
importado_api	string1	Indica se o registro foi incluído via API (S/N).+
inativo	string1	Indica se o cadastro do produto está inativo (S/N).+
componentes_kit	componentes_kitArray	Componetes do KIT.
lead_time	integer	Lead Time médio de ressuprimento em dias.
aliquota_ibpt	decimal	DEPRECATED.
cest	string9	DEPRECATED.
quantidade_estoque	decimal	DEPRECATED.
estoque_minimo	decimal	DEPRECATED.
origem_imposto	string10	Origem do Imposto+
produto_servico_cadastroArray
Este parâmetro é um array do tipo produto_servico_cadastro

Lista de produto_servico_cadastro

produto_servico_cadastro_chave
Pesquisa de produtos

codigo_produto	integer	Código do produto.+
codigo_produto_integracao	string60	Código de integração do produto.+
codigo	string60	Código do Produto.+
produto_servico_list_request
Lista os produtos cadastrados

pagina	integer	Número da página retornada
registros_por_pagina	integer	Número de registros retornados na página.
apenas_importado_api	string1	Exibir apenas os registros gerados pela API.+
ordenar_por	string100	Ordem de exibição dos dados. Padrão: Código.
ordem_decrescente	string1	Se a lista será apresentada em ordem decrescente (S/N).+
filtrar_por_data_de	string10	Filtrar os registros a partir de uma data.+
filtrar_por_hora_de	string8	Filtrar a partir da hora.+
filtrar_por_data_ate	string10	Filtrar os registros até uma data.+
filtrar_por_hora_ate	string8	Filtrar até a hora.+
filtrar_apenas_inclusao	string1	Filtrar apenas os registros incluídos (S/N).+
filtrar_apenas_alteracao	string1	Filtrar apenas os registros alterados (S/N).+
filtrar_apenas_omiepdv	string1	Filtrar apenas produtos marcados para venda via PDV.+
filtrar_apenas_familia	string50	Filtrar por ID da Familia de Produto.+
filtrar_apenas_tipo	string2	Código do Tipo do Item para o SPED.+
filtrar_apenas_descricao	string200	Filtro pela descrição do produto.+
filtrar_apenas_marketplace	string1	Filtrar apenas produtos marcados para venda via Market Place ou e-Commerce.+
filtrar_apenas_pdv	string1	Filtrar apenas produtos marcados para venda via Ponto de Venda (PDV).+
exibir_caracteristicas	string1	Exibir as características do produto (S/N).+
exibir_tabelas_preco	string1	Exibir as tabelas de preço do produto (S/N).+
caracteristicas	caracteristicasArray	lista de caracteristicas do produto.
produtosPorCodigo	produtosPorCodigoArray	Filtro por código do produto.+
inativo	string1	Indica se o cadastro do produto está inativo (S/N).+
ncm	string13	Código da Nomenclatura Comum do Mercosul (NCM).+
ean	string14	Código EAN (GTIN - Global Trade Item Number).+
ordem_descrescente	string1	DEPRECATED.
exibir_obs	string1	Exibir as observações do produto (S/N).+
exibir_kit	string1	Exibir os componentes do KIT (S/N).+
produto_servico_list_response
Lista de produtos encontrados no omie.

pagina	integer	Número da página retornada
total_de_paginas	integer	Número total de páginas
registros	integer	Número de registros retornados na página.
total_de_registros	integer	total de registros encontrados
produto_servico_resumido	produto_servico_resumidoArray	Cadastro reduzido de produtos
produto_servico_listfull_response
Lista completa de produtos encontrados no omie.

pagina	integer	Número da página retornada
total_de_paginas	integer	Número total de páginas
registros	integer	Número de registros retornados na página.
total_de_registros	integer	total de registros encontrados
produto_servico_cadastro	produto_servico_cadastroArray	Cadastro completo de produtos
produto_servico_lote_request
lote	integer	Número do lote
produto_servico_cadastro	produto_servico_cadastroArray	Cadastro completo de produtos
produto_servico_lote_response
Resposta do processamento do lote de produto importados.

lote	integer	Número do lote
codigo_status	string4	Código do status do processamento.+
descricao_status	text	Descrição do status do processamento.+
produto_servico_resumido
Cadastro reduzido de produtos

codigo_produto	integer	Código do produto.+
codigo_produto_integracao	string60	Código de integração do produto.+
codigo	string60	Código do Produto.+
descricao	string120	Descrição do produto.+
valor_unitario	decimal	Preço Unitário de Venda.+
produto_servico_resumidoArray
Este parâmetro é um array do tipo produto_servico_resumido

Lista de produto_servico_resumido

produto_servico_status
Status de retorno do cadastro de produtos

codigo_produto	integer	Código do produto.+
codigo_produto_integracao	string60	Código de integração do produto.+
codigo_status	string4	Código do status do processamento.+
descricao_status	text	Descrição do status do processamento.+
produtosPorCodigo
codigo_produto	integer	Código do produto.+
codigo_produto_integracao	string60	Código de integração do produto.+
codigo	string60	Código do Produto.+
produtosPorCodigoArray
Este parâmetro é um array do tipo produtosPorCodigo

Lista de produtosPorCodigo

recomendacoes_fiscais
origem_mercadoria	string1	Origem da Mercadoria.+
id_preco_tabelado	integer	ID do Preço tabelado (Pauta).+
id_cest	string9	Código do CEST.+
cupom_fiscal	string1	Indica se o produto é comercializado via PDV.+
market_place	string1	Indica se o produto será comercializado via Market Place ou e-commerce (S/N)+
indicador_escala	string1	Indicador de Produção em Escala Relevante.+
cnpj_fabricante	string20	CNPJ do Fabricante da Mercadoria.+
tabelas_preco
nCodTabPreco	integer	Id da tabela de preço.
cNomeTabPreco	string50	Nome da tabela de preço.
nValorTabPreco	decimal	Valor do produto na tabela de preço.
tabelas_precoArray
Este parâmetro é um array do tipo tabelas_preco

Lista de tabelas_preco

veiculo
ano_fabr	string4	Veículos - Ano de Fabricação
ano_modelo	string4	Ano modelo de fabricação
chassi	string17	Chassi do veículo
cilin	string4	Cilindradas
cmt	string9	Capacidade máxima de tração
cond_veic	string1	Condição do veículo
cod_cor_veic	string4	Código da cor do veículo
cod_cor_den	string2	Código da cor DENATRAN
descr_cor	string40	Descrição da cor
dist_eixo	string4	Distância entre eixos
especie_veic	string1	Espécie do veículo
lota_max	string3	Capacidade máxima de lotação
cod_modelo	string6	Código marca modelo
motor	string21	Número do motor
peso_bruto_veic	string9	Peso bruto
peso_liquido_veic	string9	Peso líquido
potencia	string4	Potência motor
serie_veic	string9	Série do veículo
tipo_comb	string2	Tipo de combustível
tipo_oper	string1	Tipo da operação
tipo_pintura	string1	Tipo de pintura
tipo_restricao	string1	Restrição
tipo_veic	string2	Tipo de veículo de acordo com a tabela RENAVAM
cond_vin	string1	Condição do VIN
videos
Lista de videos do produto.

url_video	text	URL do Video do produto.
videosArray
Este parâmetro é um array do tipo videos

Lista de videos
</documentacao-omie>

<documentacao-omie-api-python>
Inicio rápido
Api Omie SDK
*Aviso: Este projeto não tem ligação oficial com a Omie

SDK Multi Linguagem para integrar com a Omie API

License PyPI - Downloads GitHub License GitHub contributors GitHub Repo stars Documentation Status
Documentação Oficial da Omie
Recomendamos sempre consultar a documentação oficial da Omie para detalhes completos das funções disponíveis:

Omie API - Documentação Oficial

Instalação (Python)
Para instalar o pacote da Omie via pip, use o seguinte comando:

pip install api-omie
Como usar
Veja abaixo como fazer uma chamada básica para listar produtos usando a Omie API.

Exemplo de uso básico
from omieapi import Omie

omie_app = Omie('sua_app_key', 'seu_app_secret')
response = omie_app.listar_produtos(pagina=1)

print(response)
Os metodos se encontram neste formato nome_da_chamada(**argumentos)

Usando Sessões para Melhor Desempenho
Se você for fazer várias requisições à API, é altamente recomendado usar uma sessão para reutilizar a conexão e reduzir o overhead de abrir novas conexões a cada chamada. Veja como abrir e fechar uma sessão:

from omieapi import Omie

omie_app = Omie('sua_app_key', 'seu_app_secret', session=True)
response = omie_app.listar_produtos(pagina=1)
omie_app.fechar_session()

print(response)
O SDK também oferece suporte ao uso de gerenciador de contexto para abrir e fechar sessões automaticamente. Todas as chamadas com gerenciador de contexto tem por padrão o uso da sessão.

from omieapi import Omie
omie_app = Omie('sua_app_key', 'seu_app_secret')

with omie_app as r:
    response = r.listar_produtos(pagina=1)

print(response)
É possível abrir uma sessão utilizando o metodo Omie.abrir_sessão()

Exemplo de uso com httpx
from omieapi import Omie

omie_app = Omie('sua_app_key', 'seu_app_secret', use_httpx=True)
response = omie_app.listar_produtos(pagina=1)

print(response)
Ativando Logs para Depuração
from omieapi import Omie

omie_app = Omie('sua_app_key', 'seu_app_secret', log=True)
response = omie_app.listar_produtos(pagina=1)

print(response)
Contribua com este Projeto
Estamos sempre em busca de melhorias! Um dos próximos passos para este SDK é torná-lo realmente multi-linguagem, com suporte a diferentes linguagens de programação. Já existe um script de scraping que extrai os tipos complexos da API, mas ainda precisamos de ajuda para gerar o código de maneira automatizada.

Como Contribuir
Clone o repositório

Crie uma nova branch para suas mudanças

Envie um pull request

</documentacao-omie-api-python>

