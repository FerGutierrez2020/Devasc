curl --insecure  \
     --include \
     --header 'Content-Type:application/json' \
     --header 'Accept: application/json' \
     --user user1:cisco123 \
     --request POST https://10.10.20.70:9060/ers/config/endpoint \
     --data '
{
  "ERSEndPoint" : {
    "name" : "Assets_Endpoint",
    "description" : "Another asset",
    "mac" : "00:01:02:03:04:05",
    "groupId" : "ded3aee0-4f68-11eb-a91f-ae049b1ca50f",
    "staticGroupAssignment" : true
  }
}'