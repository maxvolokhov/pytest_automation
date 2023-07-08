doc = '''Write 30 XPATH locators for this page using XPath Axes and Wildcards. Some of them should have more than 
3 steps.
For 10 XPATH locators write 10 CSS locators which find the same element'''

url = 'https://www.apple.com/'

# 30 Xpath locators
search_button = '//a[@id="globalnav-menubutton-link-search"]'
learn_more_text_for_macbook = '''//a[@class="icon icon-after icon-chevronright"][@href="/macbook-air-13-and-15-m2/"]
[text()="Learn more"]'''
apple_logo = '//a[@href="/"][@class="globalnav-link globalnav-link-apple"]'
burger_menu_button = '//div/button[@id="globalnav-menutrigger-button"]'
entertainment_button = '//div/h3/button[@aria-controls="footer-directory-column-section-entertainment"]'
bag_button = '//a[@id="globalnav-menubutton-link-bag"]'
sixth_item_of_slide = '//a[@href="#tv-plus-gallery-item-6"]'
item_select = '//span[@id="ac-ls-dropdown-title"]/parent::div'
here_link = '//span[@id="footnote-1"]/child::a'
country_select = '//div[@class="ac-gf-footer-locale"]/child::a'
phrase_for_mac_or_ipad = '''//div[@class="dd-billboard-info"]/child::h2
[@class="dd-billboard-header dd-compact-right-large-20"]'''
find_apple_store_footer = '//div[@class="ac-gf-footer-shop"]/child::a[@href="/retail/"]'
site_map = '//a[@href="/sitemap/"]'
privacy_policy = '//a[@href="/legal/privacy/"]'
wallet_section = '//a[@class="ac-gf-directory-column-section-link"] [@href="/wallet/"]'
copy_right = '//div[@class="ac-gf-footer-legal-copyright"]'
support_in_header = '''//span[@class="globalnav-link-text-container"]/parent::a
[@href="https://support.apple.com/?cid=gn-ols-home-hp-tab"]'''
support_link = 'a[@href="https://support.apple.com/kb/HT209218"]'
airpods_section_header = '//li[@class="globalnav-submenu-trigger-item"]/child::a[@href="/airpods/"]'
for_business_section = '//h3/span[@class="ac-gf-directory-column-section-title-text"][text()="For Business"]'
mac_section_header = '//a[@href="/mac/"]/span[@class="globalnav-link-text-container"]'
ipad_section_header = '//a[@href="/ipad/"]/span[@class="globalnav-link-text-container"]'
iphone_section_header = '//a[@href="/iphone/"]/span[@class="globalnav-link-text-container"]'
manage_your_apple_id = '//li[@class="ac-gf-directory-column-section-item"]/a[@href="https://appleid.apple.com/us/"]'
contact_apple_footer = '//a[@href="/contact/"]'
apple_cash = '//a[@href="/apple-cash/"]'
vision_header_section = '//a[@href="/apple-vision-pro/"]/span[@class="globalnav-link-text-container"]'
play_pause_slide_button = '//button[@class="play-pause show paused"]'
terms_of_use_footer = '//a[@href="/legal/internet-services/terms/site.html"]'
shop_for_government_footer = '//li[@class="ac-gf-directory-column-section-item"]/child::a[text()="Shop for Government"]'

# 10 CSS locators
entertainment_button_css = 'a[href="/entertainment/"]>span.globalnav-link-text-container'
wallet_section_css = 'a[href="/wallet/"].ac-gf-directory-column-section-link'
ipad_section_header_css = 'a[href="/ipad/"]>span.globalnav-link-text-container'
apple_cash_css = 'a[href="/apple-cash/"]'
shop_for_government_footer_css = 'a[data-analytics-title="shop for government"]'
site_map_css = 'a[href="/sitemap/"]'
search_button_css = '#globalnav-menubutton-link-search'
vision_header_section_css = 'a[href="/apple-vision-pro/"]>span.globalnav-link-text-container'
support_in_header_css = 'a[data-globalnav-item-name="support"]>span.globalnav-link-text-container'
privacy_policy_css = 'a[href="/legal/privacy/"]'
