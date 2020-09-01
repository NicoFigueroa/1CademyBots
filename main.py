import WikiArticleHelper
import MicrosoftResearchApi
import json
import WikipediaScrapingLibrary
import OneCademyHelper
import ContentHelper

'''

THIS IS DIRECTLY FROM THE NOTES IN THE TEAMS CHAT 

Please implement a module that iterates through each of the "Pages" in this article. Note that you need to click the nextPage button programmatically to go through multiple pages.
	Create two empty lists pagesToPropose and potentialPages.
	For each Wikipedia article (page), call IsWikipageAppropriate to figure out whether to include the page and get its metadata.
	
		
Retrieve the list of prerequisites, using the module that Figueroa, Nicolas is working on.
			Add the page to the list potentialPages
	
	Iterate through the following until the length of potentialPages does not change anymore:
		
For each article in potentialPages:
			
if there is at least one prerequisite that exists in pagesToPropose or there exists a similar node on 1Cademy (the dictionary generated from nodes.csv), then include that page in pagesToPropose.
			otherwise, include the page in potentialPages
	
	pagesToPropose at the end contains the list of pages that should be submitted as proposals to 1Cademy
'''

#Google cloud entry point
def cloud_start(request):
	start()
	return "Complete"
#TODO 
#
# This function should loop through the list of pages from GetPagesFromCategory and 
# check each page with IsArticleAppropriate
# 
# return a dictionary where the key is the Article Title i.e. http://en.wikipedia.org/wiki/[Article Title] and the value is a list of pre-requisites 
# retrieved using WikiArticleHelper.GetPrerequisitesFromArticle
def GetPotentialPages(category):
	potential_pages = []

	articles = WikiArticleHelper.GetPagesFromCategory(category)
	for article in articles:
		if WikipediaScrapingLibrary.IsWikipageAppropriate(article, "http://en.wikipedia.com/wiki/" + article):
			potential_pages.append(article)

	return potential_pages

#TODO This is the main structure of our bot
# 
# 1.Iterate through the pages returned by WikiArticleHelper.GetPagesFromCategory("Epidemiology", True)
# Regardless of the implementation it will return a list of wiki pages without 'http://en.wikipedia.org/wiki/'
#
# 2.Call WikipediaScrapingLibrary.IsWikipageAppropriate on each to determine if the article is acceptable for use
#
# 3. If the article is acceptable put it into our list of potential pages
# 
# 4. Loop through each page in the list of potential pages and see if its prerequisite node exists in 1cademy nodes
# 
# 5. If the prerequisite node exists, then we can propose the created node
# 
# 6. For each proposed node, check references from that wiki article to see if they already exist in 1Cademy.
#    If that reference does not exist, propose it
# 
# 7. After submitting the proposal, wait 5 seconds to check back and check back with 1cademy to see if the node is accepted or not
# 
# 8. If the concept node does exist, this node will only have on prerequisite link, so now we have to submit improvement proposals
# for each prerequisite existing in that wikipedia article that exist in 1cademy already
# 
#   
# 
#    
#TODO information for proposing nodes, references to 1Cademy
#     
#  id of prereq node
# Wiki as title of node
# summary as content of node
# list of citations existing on 1cademy
# list of tags that exist as nodes on 1cademy
# if that article has a header image, submit that link in the proposal
def start():
	potential_pages = GetPotentialPages("Epidemiology")
	print(potential_pages)
	for page in potential_pages:
		url = "http://en.wikipedia.org/wiki/" + page
		print(url)
		summary_paragraphs = WikiArticleHelper.getSummaryParagraphs(WikipediaScrapingLibrary.soupStructure(url))
		print(summary_paragraphs)
		print(ContentHelper.sanitize())
		break


if __name__ == '__main__':
	cloud_start(None)