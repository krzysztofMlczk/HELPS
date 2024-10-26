Wykorzystanie LLMów do generowania kodu
Efektywność różnych metod promptingu w generowaniu kodu
Efektywność metod promptingu w generowaniu kodu
Efektywność wykorzystania różnych metod promptingu do generowania kodu

PYTANIE?
Czy chcemy używać różnych strategii promptingu?
Jakie eksperymenty? Na czym?

ESSENTIALLY:
TA PRACA TO ZBUDOWANIE I ZAPUSZCZENIE MOJEGO WŁASNEGO BENCHMARKA dla LLMÓW
https://www.youtube.com/watch?v=DeIUJRd48fI

Skuteczność Wielkich Modeli Językowych w rozwiązywaniu problemów matematycznych (zagadek logicznych???) - PROBLEMÓW LOGICZNYCH (propositional logic).
ALTERNATYWA: Skuteczność LLMów w rozumowaniu dedukcyjnym (może taki dataset łatwiej stworzyć?)
- ludzie coraz bardziej polegaja na llmach, prowadzac z nimi konwersacje na rozne tematy nawet takie ważne a nawet krytyczne (np. problemy matematyczne w normalnym zyciu) dlatego warto jest wiedziec czy mozna. w ogóle polegać na tym co ten LLM wypluwa!!!
- DODATKOWO: tutaj można opisać i wykorzystać wiele różnych metod prompt engineeringu
- TESTY MANUALNE: Można zrobić testy manualne i je opisać np. każąc modelowi opisywać swój "reasoning"
- TESTY AUTOMATYCZNE: można napisać skrypt, który każe różnym modelom rozwiązywać wiele różnych zadań. Potem policzy ile dany model rozwiązał dobrze i można wyniki przedstawić w formie fajnego i przyjemnego wykresu słupkowego (POPRAWNOŚĆ ODPOWIEDZI BĘDZIE TRZEBA WALIDOWAĆ Z WYKORZYSTANIEM LLM'a?)
	- Można zbadać dodatkowo ratio - długość treści a poprawność odpowiedzi, żeby zobaczyć czy im dłuższa treść/dłuższa odpowiedź (ta co ma być poprawna) tym gorzej sobie radzą te modele
	- TRZEBA ZROBIĆ WŁASNY DATASET
	- Walidowanie to powinien być zero-shot prompting raczej, żeby łatwo zautomatyzować testy
	- Tak naprawdę część praktyczna sprowadzi się do stworzenia mojego własnego benchmarka dla LLMów
	- Można by było "nafeedować" jeden model wiedzą na temat propositional logic i zobaczyć czy radzi sobie lepiej? Albo sprawdzić na jakimś modelu stricte matematycznym??
	- ![[Pasted image 20241021134134.png]]
- CEL: **Można by to zrobić w celu zbadania umiejętności wnioskowania logicznego**
	- które kończy się faktycznym rozwiązaniem problemu a nie mydleniem oczu użytkownikom
- Można w pracy opisać metode promptingu jaka zostanie wykorzystana w testach LUB przeprowadzać testy wykorzystując różne metody promptingu
- Przemyślenia:
	- Zagadki logiczne to całkiem niezli reprezentanci problemów jakie spotykają nas w rzeczywistości - skoro ludzie coraz bardziej polegaja na LLMach w celu rozwiązanai ich problemów to przetestowanie LLMów na tak stworzonym datasecie jest dobrym validatorem!

FRAMEWORK FOR EVALUATING LLMs:
https://dev.to/guybuildingai/-top-5-open-source-llm-evaluation-frameworks-in-2024-98m
https://github.com/openai/evals

Przydatne google searche:
- https://www.google.com/search?q=propositional+logic&oq=Propositional+logic&gs_lcrp=EgZjaHJvbWUqDQgAEAAYkQIYgAQYigUyDQgAEAAYkQIYgAQYigUyDAgBEAAYQxiABBiKBTINCAIQABiRAhiABBiKBTINCAMQABiRAhiABBiKBTIHCAQQABiABDIMCAUQABgUGIcCGIAEMg0IBhAAGJECGIAEGIoFMgYIBxBFGD3SAQgyODE4ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8
- Komentarze pod tym fillmem:
	- https://www.youtube.com/watch?v=C6PeX4iKJbU
- Lista logic puzzles:
	- https://www.mathsisfun.com/puzzles/logic-puzzles-index.html
	- https://www.mathsisfun.com/puzzles/great-picnic-puzzle.html
- 🚨 http://www.jwstelly.org/CyclopediaOfPuzzles/CyclopediaOfPuzzles.php
- Kod na którym mogę się wzorować: https://github.com/declare-lab/LLM-PuzzleTest
- Źródła zagadek:
	- https://www.amazon.com/Cyclopedia-Puzzles-tricks-Conundrums-Answers/dp/0923891781
	- http://www.jwstelly.org/CyclopediaOfPuzzles/PuzzlePage.php?puzzleid=Pz47.5#Pz47.5
	- https://www.mathsisfun.com/puzzles/
	- https://www.csd.uwo.ca/~mmorenom/cs2209_moreno/slide/lec6-deduction.pdf
	- https://www.google.com/search?q=propositional+logic+puzzles&oq=propositional+logic+puzzles&gs_lcrp=EgZjaHJvbWUqDwgAEEUYOxiRAhiABBiKBTIPCAAQRRg7GJECGIAEGIoFMgYIARAjGCcyBggCECMYJzIGCAMQRRhAMggIBBAAGBYYHjIICAUQABgWGB4yCAgGEAAYFhgeMg0IBxAAGIYDGIAEGIoF0gEINTA1OWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8
	- https://brilliant.org/wiki/logical-puzzles/
	- https://www.math.uci.edu/~mathcircle/materials/Propositional_Logic_Nov24_2014.pdf
	- https://courses.grainger.illinois.edu/cs173/sp2013/B-lecture/Lectures/Lecture%2002%20-%20Propositional%20Logic%20-%20CS173%20Spring%202013.pdf
	- https://people.cs.uchicago.edu/~laci/REU07/reupuzzles2.pdf
	- syllogisms: https://community.openai.com/t/propositionsl-logic-performance/226299/2
	- https://en.wikipedia.org/wiki/Syllogism
	- deductive reasoning - rozumowanie dedukcyjne -> TAKIE BENCHMARKI JUŻ ISTNIEJĄ
		- premises - realność
		- paper: https://openreview.net/pdf?id=THSm9HyCKo
		- paper: https://openreview.net/forum?id=THSm9HyCKo
- https://www.reddit.com/r/LocalLLaMA/comments/1dq9es0/for_those_of_you_that_are_building_your_own/


TODO (all of this can be described in the paper!):
- [ ] Describe what we want to evaluate (skuteczność w rozwiązywaniu problemów logicznych)
- [ ] Describe challenges of benchmarking LLMs
	- [ ] https://youtu.be/DeIUJRd48fI?t=1220
- [ ] Decide on models:
	- [ ] we should choose only the models that perform good in similar benchmarks (see: https://youtu.be/DeIUJRd48fI?t=1314)
- [ ] Estimate cost for 4-5 main models and 1000 examples (what is the average token count for logic problem? top token count? etc?)
	- [ ] FOR TESTING WE COULD USE LOCAL LLLAMA MODEL!!! + ipynb (https://www.youtube.com/watch?v=aJ064KCr7OU)
- [ ] Describe evaluation flow
	- [ ] Diagram that describes how exactly the evaluation will work (including the fact that responses will be judged by LLM :D)
- [ ] Decide on tech stack used
	- [ ] tools: 
		- [ ] https://youtu.be/DeIUJRd48fI?t=1911
		- [ ] OUTOFTHEBOX: 
			- [ ] https://github.com/confident-ai/deepeval
			- [ ] https://docs.confident-ai.com/docs/benchmarks-introduction
			- [ ] https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation
			- [ ] https://docs.confident-ai.com/docs/guides-answer-correctness-metric
- [ ] Decide on Evaluation Metrics e.g.:
	- [ ] Correctness (if llm is correct) - llm required to validate - WE NEED A JUDGE (returns "yes" or "no" - should be GPT4)
	- [ ] Ratio of number of characters to whether LLM response was correct
		- [ ] Other ratios? E.g. how well it performed for easy/medium/hard problems
	- [ ] Latency - how long it took to respond
	- [ ] Memory Usage (possible with API usage?)
		- [ ] GPU consumption
		- [ ] CPU consumption
	- [ ] Cost
- [ ] Decide on prompting technique:
	- [ ] Should it be zero-shot (prompt with no examples) - best for cost optimization
- [ ] Prepare the dataset (golden dataset):
	- [ ] {problem: "", answer: "", difficulty: easy | medium | hard}


OTHER LINKS:
- local llms: https://www.youtube.com/watch?v=0n35ETVXY9g
- LLM Evaluation (ML Expert) - https://www.mlexpert.io/bootcamp/llm-evaluation
	- video: https://www.youtube.com/watch?v=H2DDISTgm7U
