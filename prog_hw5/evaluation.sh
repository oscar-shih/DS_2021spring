echo "==evaluating correctness=="
for i in $(seq 1 6); do
    python3 main.py --input input_${i}.json --output output_${i}.json
    python3 evaluate.py --output output_${i}.json --golden golden_${i}.json
done
