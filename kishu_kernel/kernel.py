import os
from ipykernel.ipkernel import IPythonKernel
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("KishuKernel")
file_handler = RotatingFileHandler("/Users/matsumotoryutaro/programs/KishuKernel/KishuKernel.log", maxBytes=1024*1024, backupCount=5)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


class KishuKernel(IPythonKernel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info("KishuKernelを起動しました")

        # ファイルパスの取得
        jupyter_notebook_path = os.environ.get("JPY_SESSION_NAME")
        logger.info(f"Jupyter Notebook Path: {jupyter_notebook_path}")

        self.shell.run_cell("from kishu import init_kishu")
        self.shell.run_cell(f"init_kishu('{jupyter_notebook_path}')")


if __name__ == "__main__":
    from ipykernel import kernelapp as app

    app.launch_new_instance(kernel_class=KishuKernel)
