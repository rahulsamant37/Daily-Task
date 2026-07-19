# Advanced Multiplication Tricks for Quant (CAT & HFT)

Multiplication speed is the biggest differentiator in quant interviews. Memorizing tables up to 20x20 is a prerequisite for HFT. Beyond that, use these algebraic and pattern-based shortcuts.

## 1. Leveraging Powers of 10 (Multiplying by 5, 25, 50, 125)
Instead of multiplying, multiply by a power of 10 and divide. Division by 2, 4, or 8 is mentally much faster than multiplying by 5, 25, or 125.
*   **× 5**: Multiply by 10, divide by 2. (`48 × 5` -> `480 / 2 = 240`)
*   **× 50**: Multiply by 100, divide by 2. (`64 × 50` -> `6400 / 2 = 3200`)
*   **× 25**: Multiply by 100, divide by 4. (`84 × 25` -> `8400 / 4 = 2100`)
*   **× 125**: Multiply by 1000, divide by 8. (`72 × 125` -> `72000 / 8 = 9000`)

## 2. Difference of Squares (a² - b²) = (a + b)(a - b)
This is an incredibly powerful trick for multiplying two numbers that are equidistant from a round number.
If you need to multiply `X × Y`, find the average `A`. The distance from the average to either number is `d`.
Then `X × Y = (A - d)(A + d) = A² - d²`.

**Example:** `42 × 38`
1. The average is `40`. The distance `d` is `2`.
2. This is `(40 + 2)(40 - 2)`.
3. Equation becomes `40² - 2²`.
4. `1600 - 4 = 1596`.

**Example:** `65 × 75`
1. Average is `70`, distance is `5`.
2. `70² - 5²` = `4900 - 25 = 4875`.

## 3. Base Multiplication (Numbers close to 100)
When multiplying numbers near 100 (or 1000).

**Example:** `96 × 93` (Both below 100)
1. Find deviations from 100: `96 (-4)` and `93 (-7)`.
2. Cross-subtract for the first part of the answer: `96 - 7 = 89` (or `93 - 4 = 89`). The first part is `89_ _`.
3. Multiply the deviations for the second part: `-4 × -7 = 28`.
4. Final answer: `8928`.

**Example:** `105 × 108` (Both above 100)
1. Deviations: `+5` and `+8`.
2. Cross-add: `105 + 8 = 113`.
3. Multiply deviations: `5 × 8 = 40`.
4. Final answer: `11340`.

## 4. Multiplying by 11
**Example:** `43 × 11`
1. Write the first digit: `4`
2. Add the digits `4+3 = 7`. This is the middle digit.
3. Write the last digit: `3`
4. Answer: `473`.
*(If the sum is > 9, carry the 1 over. e.g. `85 × 11` -> `8`, `8+5=13`, `5` -> `(8+1)35` -> `935`)*

## 5. Squaring Numbers Ending in 5
**Rule:** For a number ending in 5, multiply the first digit by itself plus one. Append `25` to the end.
**Example:** `65²`
1. First digit is `6`.
2. Multiply by the next integer up: `6 × 7 = 42`.
3. Append `25`.
4. Answer: `4225`.

## 6. Squaring Any Two-Digit Number: (a+b)² = a² + 2ab + b²
You can mentally compute squares using the algebraic expansion. Treat `a` as the tens place (e.g., 40) and `b` as the ones place (e.g., 3).

**Example:** `43²`
1. Think of it as `(40 + 3)²`
2. `40² = 1600`
3. `2 × 40 × 3 = 240`
4. `3² = 9`
5. Add them up: `1600 + 240 + 9 = 1849`.

*Alternative (Distance to nearest 10):* `a² = (a+d)(a-d) + d²`
**Example:** `43²` (Nearest ten is 40, distance `d`=3)
1. `(43+3) × (43-3) = 46 × 40`
2. `46 × 40 = 1840`
3. Add `d²` (which is `3² = 9`).
4. `1840 + 9 = 1849`.

## 7. Vertical and Crosswise (The Universal 2x2 Trick)
For any `AB × CD`.
**Example:** `23 × 41`
1. Vertically multiply the ones: `3 × 1 = 3`. (Last digit is **3**)
2. Cross multiply and add: `(2 × 1) + (3 × 4) = 2 + 12 = 14`. (Write down **4**, carry over **1**)
3. Vertically multiply the tens: `2 × 4 = 8`. Add the carried `1` to get **9**.
4. Answer: **943**.
