from kishu_kernel.kernel import KishuKernel
from ipykernel import kernelapp as app

if __name__ == "__main__":
    app.launch_new_instance(kernel_class=KishuKernel)
