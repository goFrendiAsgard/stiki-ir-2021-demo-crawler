echo "[" > hasil.json
for KEYWORD in "sepeda" "fixie" "masker"
do
    URL="https://api.bukalapak.com/searches/suggestions?word=${KEYWORD}&access_token=pXZBFJn14JRN47ouN4ZIF7vZWfxRDFPi8Vy66_4REBHZLg"
    curl --location --request GET "${URL}" \
    --header 'Cookie: __cfduid=d812448bce8383a32a3ced455a794b0cd1615366991' >> hasil.json
    echo "," >> hasil.json

    sleep 1
done
echo "]" >> hasil.json