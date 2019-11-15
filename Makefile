init_submodule:
	git submodule update --init

proto: init_submodule
	python3 -m grpc_tools.protoc -I./mhist/proto --python_out=./SLAM/mhist_api --grpc_python_out=./SLAM/mhist_api ./mhist/proto/rpc.proto
