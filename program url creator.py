root = os.getcwd()
start_url = URL()
p = os.path.join(root, 'Company_Lists', 'Test_of_company.csv')
start_url.read(p)

class company-spider(BaseSpider):
    name = "Company-page"
    allowed_domains = ["CompanyDomain.se"]
    start_urls = [start_url.company-site()]
