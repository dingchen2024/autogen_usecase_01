import autogen

llm_config_local = {"config_list": [{
    "model": "llama3", 
    "base_url": "http://localhost:1234/v1",
    "api_type": "open_ai",
    "api_key": "lm-studio"
}]}


bob = autogen.AssistantAgent(
    name="Bob",
    system_message="You love telling jokes. After Alice feedback improve the joke. Say 'TERMINATE' when you have improved the joke.",
    llm_config=llm_config_local
)

alice = autogen.AssistantAgent(
    name="Alice",
    system_message="Criticise the joke.",
    llm_config=llm_config_local
)

def termination_message(msg):
    return "TERMINATE" in str(msg.get("content", ""))

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    code_execution_config={"use_docker": False},
    is_termination_msg=termination_message,
    human_input_mode="NEVER",
    system_message="your turn",
    llm_config=llm_config_local
)

groupchat = autogen.GroupChat(
    agents=[bob, alice, user_proxy],
    speaker_selection_method="round_robin",
    messages=[]
)

manager = autogen.GroupChatManager(
    groupchat=groupchat, 
    code_execution_config={"use_docker": False},
    llm_config=llm_config_local,
    is_termination_msg=termination_message
)

user_proxy.initiate_chat(
    manager, 
    message="Tell me a joke?",
)
