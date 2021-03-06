import scrapy


class DoctoraliaSpider(scrapy.Spider):
    name = 'doctoralia'
    allowed_dmains = 'www.doctoralia.com.br'
    start_urls = [
        'https://www.doctoralia.com.br/especializacoes-medicas'
    ]

    def parse(self, response):  # funcao de callback
        especialidades = response.xpath(
            '//a[re:test(@href, "https://www.doctoralia.com.br/especializacoes-medicas/")]/@href').getall()
        for especialidade in especialidades:
            yield scrapy.Request(
                especialidade,
                callback=self.parse_espec_cidade
            )

    def parse_espec_cidade(self, response):
        """ especialidades por cidades """
        espec_cidades = response.xpath(
            "//ul[@class='list-unstyled row']//a//@href").getall()
        for espec_cidade in espec_cidades:
            yield scrapy.Request(
                response.urljoin(espec_cidade),
                callback=self.parse_medico_cidade
            )

    def parse_medico_cidade(self, response):
        """ medicos por cidade """
        medicos_cidades = response.xpath(
            "//ul[@class='search-list list-unstyled']//a//@href").getall()
        for medico_cidade in medicos_cidades:
            yield scrapy.Request(
                response.urljoin(medico_cidade),
                callback=self.parse_new
            )

    def parse_new(self, response):
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
        telefone = response.css(
            'div.media:nth-child(8) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > b:nth-child(1)').get()

        yield {
            'titulo': titulo,
            'nome': nome,
            'especialidade': especialidade,
            'competencias': competencias,
            'estado': estado,
            'cidade': cidade,
            'telefone': telefone
        }
