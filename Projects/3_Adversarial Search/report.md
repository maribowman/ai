# Build an Adversarial Game Playing Agent

## Custom-Agent Performance

| Agent | Baseline | Opening Book |
| --- | --- | --- |
| Random | 94.2 % | 94.5 % |
| Greedy | 82.5 % | 92.5 % |
| Minimax | 65.0 % | 71.0 % |
| Self | 50.2 % | 55.0 % |

_*_ Results were gathered running `python3.5 run_match.py -f -r 100 -o $AGENT`

## Experiment - Opening Book

- Describe your process for collecting statistics to build your opening book. How did you choose states to sample? And
  how did you perform rollouts to determine a winner?
    - Answer: For every combination of the first 4 plies, 5 rounds were simulated. The best moves were determined by a
      win vs loss fitness. Finally, the quality of the opening could be improved by reducing noise (e.g. by including symmetries).

- What opening moves does your book suggest are most effective on an empty board for player 1 and what is player 2's
  best reply?
    - Answer: The most effective opening move is near the center of the board (5, 3) with (5, 0) being player2's best
      response.
