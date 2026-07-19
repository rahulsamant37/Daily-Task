# Advanced Division Tricks for Quant (CAT & HFT)

Division is fundamentally about recognizing patterns and converting them into multiplication or percentages. Memorizing fraction-to-percentage conversions is non-negotiable for CAT and HFT.

## 1. Memorize Reciprocals (Fractions to Percentages)
In CAT Data Interpretation or HFT probability calculations, you rarely do long division. You multiply by the reciprocal. You MUST memorize these:

*   1/2 = 50%
*   1/3 = 33.33%
*   1/4 = 25%
*   1/5 = 20%
*   1/6 = 16.66%
*   1/7 = 14.28% (Notice 14, and 14×2=28)
*   1/8 = 12.5%
*   1/9 = 11.11%
*   1/10 = 10%
*   1/11 = 9.09% (Notice multiples of 9)
*   1/12 = 8.33%
*   1/13 ≈ 7.69%
*   1/14 ≈ 7.14% (Half of 1/7)
*   1/15 = 6.66%
*   1/16 = 6.25% (Half of 1/8)

**Usage Example:** Calculate `240 / 6`.
Instead of dividing, think `240 × (1/6)`. You know `1/6` is roughly 16.6%. But more simply, if you need to calculate `210 / 7`, you know it's `30`.

**HFT Example:** What is `140 / 8`?
Think: `140 × 12.5%`. 
`140 × 10% = 14`. 
`140 × 2.5% = 3.5`.
`14 + 3.5 = 17.5`.

## 2. Converting Division to Multiplication (Powers of 5)
Just as with multiplication, dividing by 5, 25, or 125 should be converted to multiplication.

*   **÷ 5**: Multiply by 2, divide by 10. (`235 / 5` -> `235 × 2 = 470`, `470 / 10 = 47`)
*   **÷ 25**: Multiply by 4, divide by 100. (`1200 / 25` -> `1200 × 4 = 4800`, `4800 / 100 = 48`)
*   **÷ 50**: Multiply by 2, divide by 100. (`350 / 50` -> `350 × 2 = 700`, `700 / 100 = 7`)
*   **÷ 125**: Multiply by 8, divide by 1000. (`6000 / 125` -> `6000 × 8 = 48000`, `48000 / 1000 = 48`)

## 3. The "Halve and Halve Again" Method
When dividing by multiples of 2 (4, 8, 16), sequentially halve the number.

**Example:** `348 / 4`
1. Halve it once (divide by 2): `174`
2. Halve it again (divide by 2): `87`.

**Example:** `624 / 8`
1. Halve once: `312`
2. Halve twice: `156`
3. Halve thrice: `78`.

## 4. Divisibility Rules (For quick factoring)
Extremely useful for simplifying fractions before doing the actual division.
*   **Div by 3**: Sum of digits is divisible by 3. (e.g., `147`: 1+4+7 = 12. 147 is divisible by 3).
*   **Div by 4**: Last two digits form a number divisible by 4. (e.g., 3**16**).
*   **Div by 6**: Must be even AND divisible by 3.
*   **Div by 8**: Last three digits form a number divisible by 8. (Or, halve it and see if the result is divisible by 4).
*   **Div by 9**: Sum of digits is divisible by 9.
*   **Div by 11**: Alternating sum of digits is divisible by 11. (e.g., `2728`: (2+2) - (7+8) = 4 - 15 = -11. Yes, divisible).

## 5. Division by 9 (A Magic Trick)
When dividing a number by 9, the quotient and remainder follow a beautiful pattern.

**Example:** `413 / 9`
1. Bring down the first digit: **4** (This is the first digit of the quotient).
2. Add that `4` to the next digit (`1`): `4 + 1 = 5`. (This is the second digit of the quotient).
3. Add that `5` to the next digit (`3`): `5 + 3 = 8`. (This is the remainder).
**Answer:** Quotient = 45, Remainder = 8. (So, `45 8/9`).

*Note: If the remainder comes out to 9 or more, you must carry over to the quotient.*

## 6. Approximation via Percentage Shifts (Crucial for CAT DI)
If you need to calculate `432 / 815` in CAT Data Interpretation, do NOT calculate it exactly.
1. The denominator is roughly `800`.
2. `800 / 2 = 400` (which is 50%).
3. The numerator `432` is `32` higher than `400`.
4. What is `32` out of `800`? `8 × 4 = 32`, so it's `4%`.
5. Therefore, `432 / 815` is very close to `50% + 4% = 54%`. (Actual is ~53.0%).
