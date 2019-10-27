from klein import Klein
from app.pipelines import Pipeline
from app.urls import URLFinder


app = Klein()


@app.route("/")
def home(request):

    """
    A welcome function used for testing
    :return: string
    """

    return "Welcome to the Company2Vec API!"


@app.route("/company/<company_name>", methods=['GET'])
def create_embedding(request, company_name):

    """
    Creates embedding after scrape
    :param company_name: string of company name
    :return:
    """

    url = URLFinder().run(company=company_name)
    result = Pipeline(overwrite=False).run(url=url)

    return result


if __name__ == '__main__':
    app.run('localhost', port=5000)