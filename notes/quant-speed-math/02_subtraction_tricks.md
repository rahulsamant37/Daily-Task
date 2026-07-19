# Advanced Subtraction Tricks for Quant (CAT & HFT)

Subtraction can often feel more cumbersome than addition. The secret is turning subtraction into addition or leveraging round numbers to minimize "borrowing," which is very slow mentally.

## 1. Left-to-Right Subtraction
Just like addition, perform subtraction from left to right. This helps you establish the magnitude of the answer immediately.

**Example:** `834 - 357`
1. Hundreds: `834 - 300 = 534`
2. Tens: `534 - 50 = 484` (Think of it as 53 - 5 = 48)
3. Ones: `484 - 7 = 477`

## 2. The "Round Up and Adjust" Method (Overshooting)
This is the most powerful technique for subtraction. Round the number you are subtracting *up* to the nearest friendly number, subtract it, and then add back the difference.

**Example:** `542 - 189`
1. Round `189` up to `200` (which is `+11`).
2. Subtract `200`: `542 - 200 = 342`.
3. Add back the `11`: `342 + 11 = 353`.

## 3. "All from 9, and the Last from 10" (Vedic Subtraction)
This is a legendary trick for subtracting any number from a base of 10, 100, 1,000, 10,000, etc. You never have to "borrow" across zeros again.
**Rule:** Subtract every digit of the number from 9, except the right-most non-zero digit, which you subtract from 10.

**Example 1:** `1,000 - 463`
1. 9 - 4 = `5`
2. 9 - 6 = `3`
3. 10 - 3 = `7`
Answer: `537`

**Example 2:** `10,000 - 3,428`
1. 9 - 3 = `6`
2. 9 - 4 = `5`
3. 9 - 2 = `7`
4. 10 - 8 = `2`
Answer: `6572`

**Example 3 (Trailing Zeros):** `1,000 - 430`
1. Apply the rule to `43` (ignore the trailing zero for a moment).
2. 9 - 4 = `5`
3. 10 - 3 = `7`
4. Append the zero: `570`.

## 4. The Cashier's Method (Counting Up)
Instead of subtracting, think of it as finding the distance between the two numbers by adding up to round benchmarks. This turns subtraction into a simple addition problem.

**Example:** `712 - 384`
Think: "How much to get from 384 to 712?"
1. 384 to 400 is `+16`.
2. 400 to 700 is `+300`.
3. 700 to 712 is `+12`.
4. Sum the distances: `16 + 300 + 12 = 328`.

## 5. Splitting Subtraction
Break the subtrahend (the number being subtracted) into parts.

**Example:** `450 - 128`
1. `450 - 100 = 350`
2. `350 - 20 = 330`
3. `330 - 8 = 322`

---
**HFT/CAT Focus:** In Data Interpretation (CAT) or quick P&L calculations (HFT), exact subtraction is sometimes less important than rapid estimation. If you need `8,342 - 4,891`, immediately see it as `8300 - 4900 = 3400`, then refine if exactness is required.
