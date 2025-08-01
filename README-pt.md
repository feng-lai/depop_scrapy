
[English](README.md) | [日本語](README-jp.md) | [العربية](README-ar.md) | [Español](README-es.md)

# Coletor de Produtos do Depop

## Visão Geral
Este script em Python automatiza a extração de informações de produtos do Depop.com usando Selenium e BeautifulSoup. Ele coleta dados como título, preço, descrição, imagens, variações e avaliações, e os organiza em formato JSON para processamento posterior.

## Principais Funcionalidades

- **Coleta Automática**: Usa Selenium WebDriver para navegar e coletar os dados
- **Detalhes Abrangentes do Produto**:
  - Título e preço do produto
  - Descrição detalhada
  - Até 8 imagens do produto
  - Variações/opções disponíveis
  - Avaliações de clientes com notas
- **Processamento de URLs de Imagem**: Extração e formatação via regex
- **Integração com JSON**:
  - Lê `upload_results.json` com os resultados de upload de imagem
  - Substitui URLs originais pelas novas
  - Gera saída final em `product_info.json`

## Implementação Técnica

- **Selenium WebDriver**: Para automação e conteúdo dinâmico
- **BeautifulSoup**: Para análise de HTML complexo
- **WebDriverWait**: Aguarda elementos carregarem antes da extração
- **JSON**: Leitura e escrita de dados
- **Tratamento de Erros**: Mecanismos robustos para garantir a execução

## Como Usar

1. Defina o URL do produto em `product_page_url`
2. Certifique-se de que o ChromeDriver está instalado via ChromeDriverManager
3. Execute o script para:
   - Abrir a página do produto
   - Extrair todos os dados necessários
   - Processar e transformar os dados
   - Gerar a saída JSON
4. O navegador será fechado automaticamente

## Estrutura de Saída (JSON)
```json
{
  "price": "extracted_price",
  "itm_name": "product_title",
  "img1" a "img8": "processed_image_names",
  "itm_dsc": "product_description",
  "cat_id": "category_id",
  "s_id": "seller_id",
  "attr": ["option1", "option2"],
  "eva": [{"name": "reviewer", "content": "review", "level": 5}]
}
