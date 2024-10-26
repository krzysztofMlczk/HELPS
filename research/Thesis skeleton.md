# WIP
## Introduction
- WHAT
- WHEN
- WHY
- MOTIVATION
consider a question like, “What were the three takeaways from the Q2 earnings call from FY 23? Focus on the technological moats that the company is building”. This is the type of question a financial analyst would want answered to include in their reports but would need to invest time to answer.

How do we develop a solution to answer a question like above? It is immediately apparent that this information requires more than a simple lookup from an earnings call. This inquiry requires planning, tailored focus, memory, using different tools, and breaking down a complex question into simpler sub-parts~~.~~. These concepts assembled together are essentially what we have come to refer to as an LLM Agent. ([source](https://developer.nvidia.com/blog/introduction-to-llm-agents/))

# PROPOSALS
[[Sources#Conversations | FROM]]
### Thesis Structure

1. **Introduction**
    
    - **Background**: Provide an overview of LLMs and autonomous agents (e.g. [[What is LLM-powered agent?]]. Discuss how LLMs are currently used in various applications and the introduction of agents to improve efficiency.
    - **Research Problem**: Explain the core problem: What is the impact of LLM agents on the efficiency and performance of LLMs? Highlight challenges with traditional LLM usage (e.g., high resource consumption, slow inference, etc.).
    - **Objectives**: Outline the thesis' objectives, such as evaluating the efficiency of LLMs with and without agent-based assistance, measuring improvements, and analyzing potential trade-offs.
    - **Research Questions**:
        - How do LLM agents modify the efficiency of LLMs in various applications?
        - What key performance metrics (e.g., speed, resource usage, accuracy) are impacted?
        - What are the limitations or drawbacks of using LLM agents?
2. **Literature Review**
    
    - **Overview of LLMs**: Discuss the evolution of large language models, including BERT, GPT series, and their architecture, scalability, and challenges (e.g., computational cost).
    - **LLM Agents**: Define autonomous agents in the context of LLMs. Provide examples of agent-based systems (e.g., AutoGPT, BabyAGI) and discuss their theoretical purpose—improving task efficiency through automation and task delegation.
    - **Previous Studies on Efficiency**: Explore previous research on improving LLM efficiency through model compression, parallelization, or agent usage. You may also want to look at multi-agent systems and their impact on complex problem-solving.
3. **Methodology**
    
    - **Research Design**: Will you be conducting simulations, experiments, or benchmarking tasks to compare LLM performance with and without agents? Define your approach.
    - **Data Collection**: Describe the datasets or tasks you will use to evaluate LLM efficiency (e.g., text generation, summarization, code completion).
    - **Metrics for Efficiency**: Identify key metrics, such as processing time, inference speed, resource (GPU, memory) consumption, and task success rate.
    - **Tools**: Mention any frameworks, models, or software you plan to use (e.g., GPT-4, AutoGPT framework, Hugging Face libraries).
4. **Experiments and Results**
    
    - **Baseline LLM Performance**: Provide data on LLM performance in a standalone environment.
    - **LLM Agent-Enhanced Performance**: Compare the results of using LLM agents (e.g., task distribution, autonomous task completion) versus the baseline.
    - **Efficiency Analysis**: Use statistical methods to analyze the results—identify improvements in speed, cost savings, or increased accuracy and contextual understanding.
5. **Discussion**
    
    - **Interpretation of Results**: Discuss how the introduction of agents impacts efficiency. Which tasks benefit the most from agent assistance? Are there any tasks where agent-based systems underperform?
    - **Challenges and Limitations**: Highlight any drawbacks you observed, such as increased complexity or new bottlenecks caused by LLM agents (e.g., communication overhead between agents).
6. **Conclusion**
    
    - **Summary of Findings**: Summarize the key findings regarding efficiency improvements and challenges introduced by LLM agents.
    - **Future Research**: Suggest areas for further exploration, such as refining agent architectures, improving real-time decision-making, or focusing on low-resource LLM agent systems.
7. **References**
    
    - Make sure to use recent papers, books, and articles from credible sources. Cite research on LLMs, LLM agents, efficiency metrics, and multi-agent systems.