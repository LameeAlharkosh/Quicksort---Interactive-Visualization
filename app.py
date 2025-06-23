import streamlit as st
import pandas as pd
import time
from algorithm import quicksort_with_steps
from utils import plot_array_state

# ----------------------------------------
# Page configuration
# ----------------------------------------
st.set_page_config(page_title="Quicksort Visualizer", layout="centered")

# ----------------------------------------
# Sidebar: user settings
# ----------------------------------------
st.sidebar.title("🔧 Settings")

array_input = st.sidebar.text_input(
    "Array (comma-separated):", 
    "10, 5, 3, 8, 4, 2, 9, 1"
)

pivot_strategy = st.sidebar.selectbox(
    "Pivot Strategy:",
    ["First Element", "Last Element", "Median Element", "Random"]
)

delay = st.sidebar.slider(
    "Animation Speed (delay per step in seconds):", 
    min_value=0.0, 
    max_value=0.5, 
    value=0.05, 
    step=0.01
)

with st.sidebar.form("sort_form"):
    run_sort = st.form_submit_button("▶️ Run Quicksort")

# ----------------------------------------
# Main title
# ----------------------------------------
st.title("📊 Quicksort Visualization")

# ----------------------------------------
# Parse and validate input
# ----------------------------------------
try:
    array = [int(x.strip()) for x in array_input.split(',') if x.strip()]
except ValueError:
    st.error("Please enter a valid list of integers separated by commas.")
    array = []

# ----------------------------------------
# Execute on button click
# ----------------------------------------
if run_sort and array:
    # Run quicksort and capture steps and timing
    sorted_array, steps, elapsed = quicksort_with_steps(
        array.copy(), strategy=pivot_strategy
    )

    # Display summary
    st.info(f"Sorting using **{pivot_strategy}** strategy.")
    st.write(f"**Execution time:** {elapsed:.6f} seconds")
    st.write(f"**Total steps recorded:** {len(steps)}")

    # Step-by-step expander
    with st.expander("Show step-by-step execution"):
        for i, state in enumerate(steps, 1):
            plot_array_state(state)
            st.write(f"Step {i}")

    # Animated replay
    placeholder = st.empty()
    for state in steps:
        with placeholder.container():
            plot_array_state(state)
        time.sleep(delay)

    st.success("✅ Sorting complete.")
    st.balloons()

    # Test Cases demonstration
    st.markdown("---")
    st.header("🧪 Test Cases Demonstration")

    test_cases = [
        {"description": "Normal case – random array", "input": [3, 1, 4, 2, 5], "expected": sorted([3, 1, 4, 2, 5])},
        {"description": "Empty array", "input": [], "expected": []},
        {"description": "Single element", "input": [42], "expected": [42]},
        {"description": "Already sorted array", "input": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5]},
        {"description": "Reverse sorted array", "input": [5, 4, 3, 2, 1], "expected": [1, 2, 3, 4, 5]},
        {"description": "Array with duplicates", "input": [2, 3, 2, 1, 3], "expected": sorted([2, 3, 2, 1, 3])},
        {"description": "Negative and positive numbers", "input": [-2, 5, 0, -1, 3], "expected": sorted([-2, 5, 0, -1, 3])},
        {"description": "All equal elements", "input": [7, 7, 7, 7, 7], "expected": [7, 7, 7, 7, 7]},
        {"description": "Large reverse-sorted (10 elements)", "input": list(range(10, 0, -1)), "expected": list(range(1, 11))},
    ]

    results = []
    for tc in test_cases:
        arr_copy = tc["input"].copy()
        sorted_out, _, _ = quicksort_with_steps(arr_copy, strategy=pivot_strategy)
        passed = (sorted_out == tc["expected"])
        results.append({
            "Description": tc["description"],
            "Input": tc["input"],
            "Expected": tc["expected"],
            "Actual": sorted_out,
            "Result": "Pass" if passed else "Fail"
        })

    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True)

    # Complexity Analysis section
    st.markdown("---")
    st.header("📈 Complexity Analysis")
    st.markdown(
        """
**Time Complexity (Big O):**

1. **Average Case – O(n log n)**
   - On average, each partition splits the array in half ⇒ recursion depth ≈ log₂(n).
   - Partitioning takes O(n) per level ⇒ total O(n log n).

2. **Worst Case – O(n²)**
   - Occurs when partitions are maximally unbalanced (e.g., sorted input with poor pivot choice).
   - Leads to O(n²) comparisons over all recursive calls.

3. **Best Case – O(n log n)**
   - Achieved when pivot choice consistently splits arrays evenly.

---

**Space Complexity (Big O):**

- **Auxiliary Space (Average):** O(log n) for recursion stack.
- **Auxiliary Space (Worst):** O(n) when recursion depth → n.
        """
    )

