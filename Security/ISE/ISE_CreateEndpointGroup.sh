curl --insecure  \
     --include \
     --header 'Content-Type:application/json' \
     --header 'Accept: application/json' \
     --user user1:cisco123 \
     --request POST https://10.10.20.70:9060/ers/config/endpointgroup  --data '
{
  "EndPointGroup" : {
    "name" : "GrupoCurl",
    "description" : "GrupoCreado usando Curl"
  }
}'