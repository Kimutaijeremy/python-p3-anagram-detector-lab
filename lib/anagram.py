# your code goes here!
class Anagram:
    """
    A class to find anagrams of a given word from a list of candidates.
    
    An anagram is a word formed by rearranging the letters of another word,
    using all the original letters exactly once.
    """
    
    def __init__(self, word):
        """
        Initialize the Anagram with a word.
        
        Args:
            word (str): The word to find anagrams for
        """
        self.word = word.lower()  # Store in lowercase for case-insensitive comparison
    
    def match(self, candidates):
        """
        Find all anagrams of the stored word from a list of candidates.
        
        Args:
            candidates (list): A list of words to check for anagrams
            
        Returns:
            list: A list of words that are anagrams of the stored word
        """
        matches = []
        
        # Get the sorted letters of the original word
        sorted_word = sorted(self.word)
        
        # Check each candidate
        for candidate in candidates:
            candidate_lower = candidate.lower()
            
            # An anagram must:
            # 1. Not be the exact same word (case-insensitive)
            # 2. Have the same letters when sorted
            if candidate_lower != self.word and sorted(candidate_lower) == sorted_word:
                matches.append(candidate)
        
        return matches


# ============================================================================
# EXAMPLES AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("ANAGRAM FINDER - DEMONSTRATION")
    print("=" * 60)
    
    # Example 1: Basic usage
    print("\n1. Basic Example:")
    print("-" * 40)
    listen = Anagram("listen")
    result = listen.match(['enlists', 'google', 'inlets', 'banana'])
    print(f"Word: 'listen'")
    print(f"Candidates: ['enlists', 'google', 'inlets', 'banana']")
    print(f"Matches: {result}")
    print(f"✓ Expected: ['inlets']")
    
    # Example 2: Multiple matches
    print("\n2. Multiple Matches:")
    print("-" * 40)
    master = Anagram("master")
    result = master.match(['stream', 'pigeon', 'maters', 'strema'])
    print(f"Word: 'master'")
    print(f"Candidates: ['stream', 'pigeon', 'maters', 'strema']")
    print(f"Matches: {result}")
    print(f"✓ Found {len(result)} anagram(s)")
    
    # Example 3: No matches
    print("\n3. No Matches:")
    print("-" * 40)
    orca = Anagram("orca")
    result = orca.match(['horse', 'zebra', 'lion'])
    print(f"Word: 'orca'")
    print(f"Candidates: ['horse', 'zebra', 'lion']")
    print(f"Matches: {result}")
    print(f"✓ Expected: []")
    
    # Example 4: Case insensitive
    print("\n4. Case Insensitive:")
    print("-" * 40)
    Orchestra = Anagram("Orchestra")
    result = Orchestra.match(['cashregister', 'Carthorse', 'radishes'])
    print(f"Word: 'Orchestra'")
    print(f"Candidates: ['cashregister', 'Carthorse', 'radishes']")
    print(f"Matches: {result}")
    print(f"✓ Case doesn't matter!")
    
    # Example 5: Same word should not match itself
    print("\n5. Identical Words Don't Match:")
    print("-" * 40)
    corn = Anagram("corn")
    result = corn.match(['corn', 'dark', 'Corn', 'rank', 'CORN', 'cron', 'park'])
    print(f"Word: 'corn'")
    print(f"Candidates: ['corn', 'dark', 'Corn', 'rank', 'CORN', 'cron', 'park']")
    print(f"Matches: {result}")
    print(f"✓ 'corn', 'Corn', and 'CORN' excluded (same word)")
    print(f"✓ 'cron' included (different word, same letters)")
    
    # Example 6: Complex example
    print("\n6. Complex Example:")
    print("-" * 40)
    allergy = Anagram("allergy")
    candidates = ['gallery', 'ballerina', 'regally', 'clergy', 'largely', 'leading']
    result = allergy.match(candidates)
    print(f"Word: 'allergy'")
    print(f"Candidates: {candidates}")
    print(f"Matches: {result}")
    
    print("\n" + "=" * 60)
    print("HOW IT WORKS")
    print("=" * 60)
    
    explanation = """
    Algorithm:
    ----------
    1. Store the word in lowercase for case-insensitive comparison
    
    2. For each candidate word:
       a. Convert candidate to lowercase
       b. Check if it's NOT the exact same word (excluding same word)
       c. Sort both words' letters and compare
       
    3. If sorted letters match, it's an anagram!
    
    Example breakdown:
    ------------------
    Word: "listen"
    Sorted: ['e', 'i', 'l', 'n', 's', 't']
    
    Candidate: "inlets"
    Sorted: ['e', 'i', 'l', 'n', 's', 't']
    
    Match! ✓ (same sorted letters)
    
    Candidate: "google"
    Sorted: ['e', 'g', 'g', 'l', 'o', 'o']
    
    No match ✗ (different sorted letters)
    """
    
    print(explanation)
    
    print("\n" + "=" * 60)
    print("TRY IT YOURSELF!")
    print("=" * 60)
    print("\nCreate your own Anagram instance:")
    print("  my_anagram = Anagram('your_word')")
    print("  matches = my_anagram.match(['word1', 'word2', 'word3'])")
    print("=" * 60)