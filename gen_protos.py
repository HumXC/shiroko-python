import os
import subprocess


def generate_grpc_code(proto_dir, out_dir):
    protos_init_file = os.path.join(out_dir, "protos", "__init__.py")
    protos_init = ""
    # 确保输出目录存在
    os.makedirs(out_dir, exist_ok=True)

    # 遍历目录及其子目录中的所有 .proto 文件
    for root, dirs, files in os.walk(proto_dir):
        for file in files:
            if not file.endswith(".proto"):
                continue
            proto_path = os.path.join(root, file)
            base_name = os.path.splitext(file)[0]
            protos_init += f"from .{base_name} import *\n"
            # 生成gRPC代码
            subprocess.run(
                [
                    "python",
                    "-m",
                    "grpc_tools.protoc",
                    "-I.",
                    "--python_out=" + out_dir,
                    "--pyi_out=" + out_dir,
                    "--grpc_python_out=" + out_dir,
                    proto_path,
                ],
                check=True,
            )
            # 创建 __init__.py 文件
            init_file: str = os.path.join(out_dir, "protos", base_name, "__init__.py")
            os.makedirs(os.path.dirname(init_file), exist_ok=True)
            with open(init_file, "w", encoding="utf-8") as f:
                f.write(f"from .{base_name}_pb2 import *\n")
                f.write(f"from .{base_name}_pb2_grpc import *\n")
            # 修改生成的文件的包导入
            # 将 "from protos" 替换为 "from ."
            pb2_py = os.path.join(out_dir, "protos", base_name, f"{base_name}_pb2.py")
            pb2_pyi = pb2_py + "i"
            pb2_grpc_py = os.path.join(
                out_dir, "protos", base_name, f"{base_name}_pb2_grpc.py"
            )
            for file in [pb2_py, pb2_pyi, pb2_grpc_py]:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()
                    content = content.replace("from protos", "from .")
                with open(file, "w", encoding="utf-8") as f:
                    f.write(content)
    # 写入 protos/__init__.py
    with open(protos_init_file, "w", encoding="utf-8") as f:
        f.write(protos_init)


if __name__ == "__main__":
    PROTO_DIR = "./protos"
    OUT_DIR = "./src"
    generate_grpc_code(PROTO_DIR, OUT_DIR)
