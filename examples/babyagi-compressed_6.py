1:import,2:openai,3:pinecone,4:OPENAI_API_KEY,5:PINECONE_API_KEY,6:PINECONE_ENVIRONMENT,7:Pinecone,8:YOUR_TABLE_NAME,9:OBJECTIVE,10:YOUR_FIRST_TASK,11:api_key,12:Create,13:table_name,14:dimension,15:metric,16:pod_type,17:task_list,18:add_task,19:append,20:get_ada_embedding,21:return,22:create,23:embedding,24:task_creation_agent,25:objective,26:result,27:task_description,28:prompt,29:execution,30:following,31:completed,32:incomplete,33:Return,34:response,35:Completion,36:engine,37:davinci,38:temperature,39:max_tokens,40:frequency_penalty,41:presence_penalty,42:new_tasks,43:choices,44:task_name,45:prioritization_agent,46:this_task_id,47:task_names,48:next_task_id,49:task_string,50:task_parts,51:task_id,52:execution_agent,53:context,54:context_agent,55:query_embedding,56:results,57:sorted_results,58:first_task,59:task_id_counter,60:enriched_result,61:result_id,62:vector,63:new_task,
\1\ \2\
\1\ \3\
\1\ time
from collections \1\ deque
from typing \1\ Dict, List

#Set API Keys
\4\ = ""
\5\ = ""
\6\ = "us-east1-gcp" #\7\ Environment (eg. "us-east1-gcp")

#Set Variables
\8\ = "test-table"
\9\ = "Solve world hunger."
\10\ = "Develop a task list."

#Print \9\
print("\033[96m\033[1m"+"\n*****\9\*****\n"+"\033[0m\033[0m")
print(\9\)

# Configure OpenAI and \7\
\2\.\11\ = \4\
\3\.init(\11\=\5\, environment=\6\)

# \12\ \7\ index
\13\ = \8\
\14\ = 1536
\15\ = "cosine"
\16\ = "p1"
if \13\ not in \3\.list_indexes():
    \3\.create_index(\13\, \14\=\14\, \15\=\15\, \16\=\16\)

# Connect to the index
index = \3\.Index(\13\)

# Task list
\17\ = deque([])

def \18\(task: Dict):
    \17\.\19\(task)

def \20\(text):
    text = text.replace("\n", " ")
    \21\ \2\.Embedding.\22\(input=[text], model="text-\23\-ada-002")["data"][0]["\23\"]

def \24\(\25\: str, \26\: Dict, \27\: str, \17\: List[str]):
    \28\ = f"You are an task creation AI that uses the \26\ of an \29\ agent to \22\ new tasks with the \30\ \25\: {\25\}, The last \31\ task has the \26\: {\26\}. This \26\ was based on this task description: {\27\}. These are \32\ tasks: {', '.join(\17\)}. Based on the \26\, \22\ new tasks to be \31\ by the AI system that do not overlap with \32\ tasks. \33\ the tasks as an array."
    \34\ = \2\.\35\.\22\(\36\="text-\37\-003",\28\=\28\,\38\=0.5,\39\=100,top_p=1,\40\=0,\41\=0)
    \42\ = \34\.\43\[0].text.strip().split('\n')
    \21\ [{"\44\": \44\} for \44\ in \42\]

def \45\(\46\:int):
    global \17\
    \47\ = [t["\44\"] for t in \17\]
    \48\ = int(\46\)+1
    \28\ = f"""You are an task prioritization AI tasked with cleaning the formatting of and reprioritizing the \30\ tasks: {\47\}. Consider the ultimate \25\ of your team:{\9\}. Do not remove any tasks. \33\ the \26\ as a numbered list, like:
    #. First task
    #. Second task
    Start the task list with number {\48\}."""
    \34\ = \2\.\35\.\22\(\36\="text-\37\-003",\28\=\28\,\38\=0.5,\39\=1000,top_p=1,\40\=0,\41\=0)
    \42\ = \34\.\43\[0].text.strip().split('\n')
    \17\ = deque()
    for \49\ in \42\:
        \50\ = \49\.strip().split(".", 1)
        if len(\50\) == 2:
            \51\ = \50\[0].strip()
            \44\ = \50\[1].strip()
            \17\.\19\({"\51\": \51\, "\44\": \44\})

def \52\(\25\:str,task: str) -> str:
    #\53\ = \54\(index="quickstart", query="my_search_query", n=5)
    \53\=\54\(index=\8\, query=\25\, n=5)
    #print("\n*******RELEVANT CONTEXT******\n")
    #print(\53\)
    \34\ = \2\.\35\.\22\(
        \36\="text-\37\-003",
        \28\=f"You are an AI who performs one task based on the \30\ \25\: {\25\}. Your task: {task}\nResponse:",
        \38\=0.7,
        \39\=2000,
        top_p=1,
        \40\=0,
        \41\=0
    )
    \21\ \34\.\43\[0].text.strip()

def \54\(query: str, index: str, n: int):
    \55\ = \20\(query)
    index = \3\.Index(index_name=index)
    \56\ = index.query(\55\, top_k=n,
    include_metadata=True)
    #print("***** RESULTS *****")
    #print(\56\)
    \57\ = sorted(\56\.matches, key=lambda x: x.score, reverse=True)    
    \21\ [(str(item.metadata['task'])) for item in \57\]

# Add the first task
\58\ = {
    "\51\": 1,
    "\44\": \10\
}

\18\(\58\)
# Main loop
\59\ = 1
while True:
    if \17\:
        # Print the task list
        print("\033[95m\033[1m"+"\n*****TASK LIST*****\n"+"\033[0m\033[0m")
        for t in \17\:
            print(str(t['\51\'])+": "+t['\44\'])

        # Step 1: Pull the first task
        task = \17\.popleft()
        print("\033[92m\033[1m"+"\n*****NEXT TASK*****\n"+"\033[0m\033[0m")
        print(str(task['\51\'])+": "+task['\44\'])

        # Send to \29\ function to complete the task based on the \53\
        \26\ = \52\(\9\,task["\44\"])
        \46\ = int(task["\51\"])
        print("\033[93m\033[1m"+"\n*****TASK RESULT*****\n"+"\033[0m\033[0m")
        print(\26\)

        # Step 2: Enrich \26\ and store in \7\
        \60\ = {'data': \26\}  # This is where you should enrich the \26\ if needed
        \61\ = f"result_{task['\51\']}"
        \62\ = \60\['data']  # extract the actual \26\ from the dictionary
        index.upsert([(\61\, \20\(\62\),{"task":task['\44\'],"\26\":\26\})])

    # Step 3: \12\ new tasks and reprioritize task list
    \42\ = \24\(\9\,\60\, task["\44\"], [t["\44\"] for t in \17\])

    for \63\ in \42\:
        \59\ += 1
        \63\.update({"\51\": \59\})
        \18\(\63\)
    \45\(\46\)

time.sleep(1)  # Sleep before checking the task list again