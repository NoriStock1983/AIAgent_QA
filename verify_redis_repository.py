import sys
import os

# Add src to python path
sys.path.append(os.path.join(os.getcwd(), 'src'))

try:
    from infrastructures.repositories.redis_repository import RedisRepository
    from domain.cashe.entities.searchRedis import SearchRedis
    
    print("Initializing RedisRepository...")
    repo = RedisRepository()
    
    query = "What is Clean Architecture?"
    answer = "Clean Architecture is a software design philosophy..."
    search_redis = SearchRedis(query=query, answer=answer)
    
    print(f"Inserting data: query='{query}'")
    repo.insert(search_redis)
    
    print("Searching data...")
    result = repo.search(query)
    
    if result:
        print(f"Found: {result.answer}")
        if result.answer == answer:
            print("Verification SUCCESS")
        else:
            print("Verification FAILED: Content mismatch")
    else:
        print("Verification FAILED: Data not found")
        
    print("Searching non-existent data...")
    result_none = repo.search("Non-existent query")
    if result_none is None:
        print("Verification SUCCESS (Non-existent data)")
    else:
        print("Verification FAILED: Found data that shouldn't exist")

except Exception as e:
    print(f"An error occurred: {e}")
    import traceback
    traceback.print_exc()
