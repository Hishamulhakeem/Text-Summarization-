from summarizer import TextSummarizer

if __name__ == "__main__":
    text = """
    The Indian Space Research Organisation (ISRO) has launched Chandrayaan-3, 
    the third lunar mission in its Chandrayaan program. This mission aims to 
    demonstrate the ability to perform a soft landing on the Moon. Chandrayaan-3 
    is a follow-up to Chandrayaan-2, which failed to achieve a successful soft 
    landing. The new mission includes a lander and a rover, but does not have an orbiter.
    """

    summarizer = TextSummarizer()
    summary = summarizer.summarize(text)
    print("📝 Original:\n", text)
    print("\n🔍 Summary:\n", summary)
