# busca especialidades 
scrapy shell https://www.doctoralia.com.br/especializacoes-medicas/
response.xpath("//div[@class='display-flex justify-content-between align-items-center']//a[@class='text-muted']//@href").getall()

# busca especialidades por cidades
# scrapy shell https://www.doctoralia.com.br/especializacoes-medicas/em-detalhe/urologista
response.xpath("//ul[@class='list-unstyled row']//a//@href").getall()

# busca  lista de medicos por cidade
# scrapy shell https://www.doctoralia.com.br/urologista/sorocaba
response.xpath("//ul[@class='search-list list-unstyled']//a//@href").getall() 

# Buscar Campos
titulo = response.xpath(
            '/html/body/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/div/h1/div/span[1]//text()').get()
nome = response.xpath(
            '/html/body/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/div/h1/div/span[2]//text()').get()
especialidade = response.xpath(
            '/html/body/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/div/h2/a//text()').get()
competencias = ''
        estado = response.xpath(
            '/html/body/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/h5/span[3]//@content').get()
cidade = response.xpath(
            '/html/body/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/h5/span[2]//@content').get()
telefone = response.css('div.media:nth-child(8) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > b:nth-child(1)').get()
