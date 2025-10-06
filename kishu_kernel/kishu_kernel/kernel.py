import os
from ipykernel.ipkernel import IPythonKernel
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("KishuKernel")
file_path = "/Users/matsumotoryutaro/programs/KishuKernel/KishuKernel.log"
file_handler = RotatingFileHandler(file_path, maxBytes=1024*1024, backupCount=5)
file_handler.setFormatter(
    logging.Formatter("[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d] %(levelname)s - %(message)s")
)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


class KishuKernel(IPythonKernel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info("KishuKernelを起動しました")

        # ファイルパスの取得
        jupyter_notebook_path = os.environ.get("JPY_SESSION_NAME")
        logger.info(f"Jupyter Notebook Path: {jupyter_notebook_path}")

        self.run_cell("from kishu import init_kishu")
        self.run_cell(f"init_kishu('{jupyter_notebook_path}')")

    def run_cell(self, code):
        result = self.shell.run_cell(code)
        logger.debug(f"セルの実行結果: {result}")
        if result.error_in_exec:
            logger.error(f"セルの実行中にエラーが発生しました: {result.error_in_exec}")
        elif result.error_before_exec:
            logger.error(f"セル実行前にエラーが発生しました: {result.error_before_exec}")
        else:
            logger.info(f"セルを正常に実行しました: {code[:50]}...")
