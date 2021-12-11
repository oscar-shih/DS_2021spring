RED='\033[1;31m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color
echo "==evaluating correctness=="
for i in $(seq 1 3); do
    python BSTree.py --input input_${i}.txt --output output_${i}.txt
    dline_py=$(diff output_${i}.txt golden_${i}.txt |  wc | awk -F ' ' '{print $1}')
    if [ "${dline_py}" == "0" ] && [ -f output_${i}.txt ] && [ -f golden_${i}.txt ] ; then
        echo -e "${GREEN}BSTree.py is correct in test case: input_${i}.txt${NC}"
    else
        echo -e "${RED}BSTree.py is incorrect in test case: input_${i}.txt${NC}"
    fi
done
