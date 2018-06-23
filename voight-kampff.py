#!/usr/bin/python3

# Imports
import requests
import argparse


# Function to print assorted lists.
def print_list(disp_list):
	for element in disp_list:
		print(element)
	print("\r\n")


# Function to handle requests.
def check_access(page_list,ret=False):
	# Create lists for metrics.
	list_200 = []
	list_300 = []
	list_400 = []
	list_other = []
	
	# Iterate through passed pages, requesting each and checking the returned status code.
	for page in page_list:
		target = targ + page
		
		# Make request to https://target/page
		try:
			response = requests.get(target)
		except requests.exceptions.RequestException as e:
			print(e)
	
		status = response.status_code
		
		# Build lists for metrics
		if status == 200:
			list_200.append((target,status))
		elif status >= 300 and status < 400:
			list_300.append((target,status))
		elif status >= 400 and status < 500:
			list_400.append((target,status))
		else:
			list_other.append((target,status))

	# If the response is wanted somewhere, deliver it.
	if ret:
		return response
	else:
		print('\r\n'+'-'*50)
		print('Number of 200 OK results: {}'.format(len(list_200)))
		print_list(list_200)
		print('Number of 3XX results: {}'.format(len(list_300)))
		print_list(list_300)
		print('Number of 4XX results: {}'.format(len(list_400)))
		print_list(list_400)
		print('Number of other results: {}'.format(len(list_other)))
		print_list(list_other)


# Handle robots.txt processing.
def process_robots():
	# Create empty lists to hold results
	agent_list = []
	allowed_list = []
	disallowed_list = []

	# Grab site's robots.txt and the response.
	resp = check_access(["/robots.txt"],ret=True)
	
	# Parse robots.txt entries into lists.
	for line in resp.text.splitlines():
		elements = line.split()
		# Check if there's a value for each entry - avoid issues with "Disallow: ".
		if len(elements) > 1:
			if "User-agent" in line:
				agent_list.append(elements[1])
			elif "Allow" in line:
				allowed_list.append(elements[1])
			elif "Disallow" in line:
				disallowed_list.append(elements[1])
			else:
				pass
		else:
			pass
	
	# Remove duplicates
	agent_list = sorted(set(agent_list))
	allowed_list = sorted(set(allowed_list))
	disallowed_list = sorted(set(disallowed_list))
	
	# Print lists scraped from robots.txt.
	print("\r\nSpecified User-Agents: {}".format(len(agent_list)))
	print_list(agent_list)
	print('-'*50)

	# Check access for Allow entries.
	print('Allowed Results:')
	check_access(allowed_list)
	print('-'*50)
	
	# Check access for Disallow entries.
	print('\r\nDISallowed Results:')
	check_access(disallowed_list)


# Main function
def main():
	# Define command line arguments
	parser = argparse.ArgumentParser(description="Scrape robots.txt file and check actual page access.")
	parser.add_argument('-t', required=True, metavar='--target', help='Target URL: e.g., https://google.com')
	args = parser.parse_args()

	global targ
	targ = args.t

	# Format provided URL. TODO: handle https/http failover.
	if 'http' not in targ:
		targ = 'https://' + targ
	if targ[-1] == '/':
		targ = targ.rstrip('/')

	print("Targeting: {}\r\n{}\r\n".format(targ,'-'*50))

	# Start the real work.
	process_robots()


if __name__ == "__main__":
	main()