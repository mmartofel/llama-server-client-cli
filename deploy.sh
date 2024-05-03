
oc new-project llama-server
oc apply -k ./deployment/server -n llama-server
oc apply -k ./deployment/cli -n llama-server

