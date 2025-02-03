# Azure Integration for AI-Powered Document Querying

This Python code communicates with Azure services—Azure Search, Azure OpenAI, and Blob Storage—to create an AI that answers questions using a private document. Developed as part of my learning process, it showcases how to leverage Azure's capabilities for document indexing, storage, and natural language processing to build intelligent, context-aware applications.

![AzureOpenAI_CognitiveSearch](https://blog.cloudnative.co.jp/wp-content/uploads/2023/06/AzureOpenAI_CognitiveSearch.jpg)

TO DO

    max_tokens=800,
    stop=None,  
    extra_body={  
        "data_sources": [  
            {  
                "type": "azure_search",  
                "parameters": {  
                    "endpoint": os.environ["AZURE_AI_SEARCH_ENDPOINT"],  
                    "index_name": os.environ["AZURE_AI_SEARCH_INDEX"],  
                    "authentication": {  
                        "type": "system_assigned_managed_identity"  
                    }  
                }  
            }  
        ]  
    } 
