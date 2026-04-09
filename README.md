# Lie Detector Terminal
> A terminal-based game that claims to catch people lying

---

## What is it?
***Lie Detector Terminal*** is a fun CLI game that tries to figure out if you're lying just by using basic psychology and asking yes/no questions.

---

## How to play
Run the program. It will ask you 11 questions, and you answer those in yes or no. As simple as that!

---

## Demo
https://github.com/user-attachments/assets/3ddf55e3-d44a-4a80-b47a-ba9c2b91f5ef

---

## Detection Methods
- **How fast you answer:** Normal people answer yes/no questions pretty quickly. But when you're lying, your brain has to do extra work to cook up the answer. So if you pause even a second too long, the game clocks it and marks it against you. And just to be a bit unpredictable, the final score has a tiny bit of random noise added. So even the same answers won't always give you the same result.

- **Contradictions:** Basically it asks you similar questions at different points. not copy pasted, but close enough that your answers should line up. if they don't match, it catches you, which goes against your score.

---

## How to Run It
**Option 1 - Run with Python:**
```bash
git clone https://github.com/shams-007/Lie-detector.git
cd Lie-detector
python lie_detector.py
```
Make sure you have Python 3 installed.

**Option 2 - Download the .exe (no python needed):**

Download the exe file from the [Releases](https://github.com/shams-007/Lie-detector/releases) and run it

---

## Built with
- Python 3
- `time` 
- `random`

---

## Contribution
**You can contribute by**
- adding more interesting questions
- improving the lie detection logic
- or fix anything that bugs you

---

