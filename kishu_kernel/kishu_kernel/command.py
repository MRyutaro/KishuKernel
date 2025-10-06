import sys
from pathlib import Path


def install_kernel():
    try:
        from jupyter_client.kernelspec import install_kernel_spec
    except ImportError:
        raise ImportError("jupyter_clientがインストールされていません。")

    # kishu_kernelパッケージの実際のパスを取得
    kernel_dir = Path(__file__).parent
    install_kernel_spec(
        str(kernel_dir), kernel_name="kishu_kernel", user=True, replace=True
    )
    print(f"Kishu Kernel installed from: {kernel_dir}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "install":
        install_kernel()
    else:
        print("Usage: kishu-kernel install", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
