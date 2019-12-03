initialize:
	git submodule update --init  

generate_mhist_api:
	python3 -m grpc_tools.protoc -I./mhist/proto --python_out=./SLAM/mhist_api --grpc_python_out=./SLAM/mhist_api ./mhist/proto/rpc.proto

run:
	python3 ./main.py
