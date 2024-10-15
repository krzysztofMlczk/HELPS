## LLM-Agent components

![[Pasted image 20241013201510.png]]
[source](https://developer.nvidia.com/blog/introduction-to-llm-agents/#:~:text=Figure%201.%20General%20components%20of%20an%20agent)

### Agent Core (brain of the operation)
- Orchestrator
- Central Coordination Module
- "key decision making module"
[source](https://developer.nvidia.com/blog/introduction-to-llm-agents/#:~:text=The%20agent%20core%20is%20the%20central%20coordination%20module%20that%20manages%20the%20core%20logic%20and%20behavioral%20characteristics%20of%20an%20Agent.%20Think%20of%20it%20as%20the%20%E2%80%9Ckey%20decision%20making%20module%E2%80%9D%20of%20the%20agent.%20It%20is%20also%20where%20we%20define%3A)

### Memory module
Two types:
- Short-term memory
	- Agent's "train of thoughts" (when answering a single question)
- Long term memory
	- Actions and thoughts, past conversations etc.
[source](https://developer.nvidia.com/blog/introduction-to-llm-agents/#memory_module)

### Tools
- Executable workflows
- Used to do certain tasks
- Custom code / external APIs etc.
[source](https://developer.nvidia.com/blog/introduction-to-llm-agents/#tools)

### Planning module
- Quides and dictates:
	- Task decomposition
	- Question decomposition
	- Order of items to perform
- Different techniques for improving reasoning capabilities and responses of LLMs can be used e.g.:
	- ReAct (Reason & Act)
	- Reflexion
	- Chain of Thought
	- Graph of thought
[source](https://developer.nvidia.com/blog/introduction-to-llm-agents/#planning_module)

