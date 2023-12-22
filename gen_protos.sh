#!/usr/bin/env sh

# 安装对应的 python grpc 工具
# pip install grpcio-tools
PROTO_DIR="./protos"
OUT="./src"
# 遍历目录及其子目录中的所有 .proto 文件
for proto in $(find $PROTO_DIR -name "*.proto"); do
    # echo "Generating Go code for $proto..."
    python -m grpc_tools.protoc \
        -I. \
        --python_out=$OUT \
        --pyi_out=$OUT \
        --grpc_python_out=$OUT \
        $proto
    base=$(basename "$proto" .proto)
    # 创建 __init__.py 文件（如果尚不存在）
    init_file="$OUT/protos/$base/__init__.py"
    if [ ! -f "$init_file" ]; then
        touch "$init_file"
    fi

    # 向 __init__.py 写入导入语句
    echo -e "from .${base}_pb2 import *\nfrom .${base}_pb2_grpc import *" >"$init_file"
done
