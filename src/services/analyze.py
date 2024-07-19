import asyncio

from pylastic.elater.renderer import ElasticFunction
from pylastic.handler.exceptions import TensorNotFound
from pylastic import Tensor, Analyzer, Viewer, ElasticRender


class AnalyzeService:

    def __init__(self):
        pass

    def process_analyze(self, file: bytes, title: str = ""):
        tensor = Tensor(file)
        if not tensor.found:
            raise TensorNotFound('')
        analyzer = Analyzer(tensor)
        asyncio.run(analyzer.analyze())
        viewer = Viewer(analyzer.analyzed, title=title)
        return asyncio.run(viewer.render())

    def process_surface(self, file: bytes, function: ElasticFunction):
        tensor = Tensor(file)
        if not tensor.found:
            raise TensorNotFound('')
        analyzer = Analyzer(tensor)
        asyncio.run(analyzer.analyze())
        renderer = ElasticRender(analyzer, full_html=False, path_to_plotly_js='cdn', width=800, height=800)
        return asyncio.run(renderer.html_surface(function))

    def process_projections(self, file: bytes, function: ElasticFunction):
        tensor = Tensor(file)
        if not tensor.found:
            raise TensorNotFound('')
        analyzer = Analyzer(tensor)
        asyncio.run(analyzer.analyze())
        renderer = ElasticRender(analyzer, full_html=False, path_to_plotly_js='cdn')
        return asyncio.run(renderer.html_projections(function))