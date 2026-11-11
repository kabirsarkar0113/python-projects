# GROCERY COST COMPARISON TOOL
print("=== GROCERY COST COMPARISON TOOL ===")

# ---------- PART 1: what did this week's shop cost per person? ----------
rice_price = 12            # (given)
milk_price = 4             # (given)
fruit_price = 8            # (given)
number_of_baskets = 2      # (given)
family_members = 4         # (given)
# YOUR CODE HERE
# Add the three prices first, then multiply by the baskets, then divide by the family.
# You need parentheses. Print the result.
cost_per_person = 0        # placeholder: replace this line with your own

# ---------- PART 2: can the items be shared equally? ----------
# YOUR CODE HERE
# Ask for total_items and people. Wrap both in int().
# Use % to check: remainder 0 -> they divide equally.
# Otherwise say they do not, and show how many are left over.

# ---------- PART 3: compare with three stores ----------
weekly_average = 72.5      # (given) the corrected weekly average
store_a_average = 70       # (given)
store_b_average = 75       # (given)
store_c_average = 80       # (given)
# YOUR CODE HERE
# Use and with if / elif / else to fill verdict:
#   below all three  -> "cheaper than all three stores"
#   above all three  -> "more expensive than all three stores"
#   otherwise        -> "somewhere in between the three stores"
verdict = ""               # placeholder: replace this line with your own

print("\n=== SUMMARY ===")                                   # (given)
print("Cost per person this week:", cost_per_person)         # (given)
print("Weekly average           :", weekly_average)          # (given)
print("Verdict                  :", verdict)                 # (given)