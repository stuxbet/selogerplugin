"""Auto-generated FieldSpec rows derived from the AVIV CaaS v4 OpenAPI.

Do not edit by hand. Re-generate with:

    python -m seloger.ops.derive_fields_from_openapi

Source spec: ``seloger/context/aviv-classified-api-v4.json``.
Naming convention: each field uses the shortest snake_case suffix of its
OpenAPI path that is unique across the whole schema. Labels carry both
``en_US`` (from the OpenAPI ``title``) and ``fr_FR`` (a small set of
hand-curated overrides; falls back to the English label otherwise).
"""

from __future__ import annotations

from .fields import FieldSpec, SelectionOption


def _t(en: str, fr: str) -> dict[str, str]:
    return {"en_US": en, "fr_FR": fr}



# ---- building_property (19 fields) ----
DERIVED_BUILDING_PROPERTY_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_sales_office_postalcode',
        ttype='char',
        label=_t('Sales Office Postalcode', 'Sales Office Postalcode'),
        help=_t('postalcode or zip of the property location. It can be empty when not applicable. Use an empty string for unknown value.', 'postalcode or zip of the property location. It can be empty when not applicable. Use an empty string for unknown value.'),
        size=32,
        # source: data.buildingProperty.program.salesOffice.postalcode
    ),
    FieldSpec(
        name='x_sales_office_city',
        ttype='char',
        label=_t('Sales Office City', 'Sales Office City'),
        help=_t('city where the property is located. It can be empty when not applicable. Use an empty string for unknown value.', 'city where the property is located. It can be empty when not applicable. Use an empty string for unknown value.'),
        size=128,
        # source: data.buildingProperty.program.salesOffice.city
    ),
    FieldSpec(
        name='x_sales_office_street',
        ttype='text',
        label=_t('Sales Office Street', 'Sales Office Street'),
        help=_t('street where the property is located. It can also be a place name or any required neighbourhood information. It can be empty when not applicable. Use an empty string for unknown value.', 'street where the property is located. It can also be a place name or any required neighbourhood information. It can be empty when not applicable. Use an empty string for unknown value.'),
        # source: data.buildingProperty.program.salesOffice.street
    ),
    FieldSpec(
        name='x_sales_office_house_number',
        ttype='char',
        label=_t('Sales Office House Number', 'Sales Office House Number'),
        help=_t('house number where the property is located. It can be empty when not applicable. Use an empty string for unknown value.', 'house number where the property is located. It can be empty when not applicable. Use an empty string for unknown value.'),
        size=64,
        # source: data.buildingProperty.program.salesOffice.houseNumber
    ),
    FieldSpec(
        name='x_sales_office_country',
        ttype='char',
        label=_t('Sales Office Country', 'Sales Office Country'),
        help=_t('country where the property is located. **Note:** You are strongly encouraged to use ISO3166 country codes instead of country names. You can use the three-letter code (alpha-3) which is more closely related to the country name. ISO3166 country codes will be mandatory in the next major version.', 'country where the property is located. **Note:** You are strongly encouraged to use ISO3166 country codes instead of country names. You can use the three-letter code (alpha-3) which is more closely related to the country name. ISO3166 country codes will be mandatory in the next major version.'),
        size=125,
        # source: data.buildingProperty.program.salesOffice.country
    ),
    FieldSpec(
        name='x_promoter_name',
        ttype='char',
        label=_t('Promoter Name', 'Promoter Name'),
        help=_t('name of the promoter. It can be empty when not applicable.', 'name of the promoter. It can be empty when not applicable.'),
        size=64,
        # source: data.buildingProperty.program.coPromotion.promoter.name
    ),
    FieldSpec(
        name='x_promoter_address_street',
        ttype='char',
        label=_t('Promoter Address Street', 'Promoter Address Street'),
        help=_t('street of the promoter. It can be empty when not applicable.', 'street of the promoter. It can be empty when not applicable.'),
        size=64,
        # source: data.buildingProperty.program.coPromotion.promoter.address.street
    ),
    FieldSpec(
        name='x_promoter_address_house_number',
        ttype='char',
        label=_t('Promoter Address House Number', 'Promoter Address House Number'),
        help=_t('house number of the promoter. It can be empty when not applicable.', 'house number of the promoter. It can be empty when not applicable.'),
        size=4,
        # source: data.buildingProperty.program.coPromotion.promoter.address.houseNumber
    ),
    FieldSpec(
        name='x_promoter_address_postalcode',
        ttype='char',
        label=_t('Promoter Address Postalcode', 'Promoter Address Postalcode'),
        help=_t('postalcode or zip of the promoter. It can be empty when not applicable.', 'postalcode or zip of the promoter. It can be empty when not applicable.'),
        size=8,
        # source: data.buildingProperty.program.coPromotion.promoter.address.postalcode
    ),
    FieldSpec(
        name='x_promoter_address_city',
        ttype='char',
        label=_t('Promoter Address City', 'Promoter Address City'),
        help=_t('city of the promoter. It can be empty when not applicable.', 'city of the promoter. It can be empty when not applicable.'),
        size=32,
        # source: data.buildingProperty.program.coPromotion.promoter.address.city
    ),
    FieldSpec(
        name='x_promoter_address_country',
        ttype='char',
        label=_t('Promoter Address Country', 'Promoter Address Country'),
        help=_t('country where the promoter is located. **Note:** You are strongly encouraged to use ISO3166 country codes instead of country names. You can use the three-letter code (alpha-3) which is more closely related to the country name. ISO3166 country codes will be mandatory in the next major version.', 'country where the promoter is located. **Note:** You are strongly encouraged to use ISO3166 country codes instead of country names. You can use the three-letter code (alpha-3) which is more closely related to the country name. ISO3166 country codes will be mandatory in the next major version.'),
        size=16,
        # source: data.buildingProperty.program.coPromotion.promoter.address.country
    ),
    FieldSpec(
        name='x_promoter_url_logo',
        ttype='char',
        label=_t('Promoter Url Logo', 'Promoter Url Logo'),
        help=_t('URL to the logo of the promoter. It can be empty when not applicable.', 'URL to the logo of the promoter. It can be empty when not applicable.'),
        size=128,
        # source: data.buildingProperty.program.coPromotion.promoter.urlLogo
    ),
    FieldSpec(
        name='x_co_promoter_name',
        ttype='char',
        label=_t('Co Promoter Name', 'Co Promoter Name'),
        help=_t('name of the co-promoter. It can be empty when not applicable.', 'name of the co-promoter. It can be empty when not applicable.'),
        size=64,
        # source: data.buildingProperty.program.coPromotion.coPromoter.name
    ),
    FieldSpec(
        name='x_co_promoter_address_street',
        ttype='char',
        label=_t('Co Promoter Address Street', 'Co Promoter Address Street'),
        help=_t('street of the co-promoter. It can be empty when not applicable.', 'street of the co-promoter. It can be empty when not applicable.'),
        size=64,
        # source: data.buildingProperty.program.coPromotion.coPromoter.address.street
    ),
    FieldSpec(
        name='x_co_promoter_address_house_number',
        ttype='char',
        label=_t('Co Promoter Address House Number', 'Co Promoter Address House Number'),
        help=_t('house number of the co-promoter. It can be empty when not applicable.', 'house number of the co-promoter. It can be empty when not applicable.'),
        size=4,
        # source: data.buildingProperty.program.coPromotion.coPromoter.address.houseNumber
    ),
    FieldSpec(
        name='x_co_promoter_address_postalcode',
        ttype='char',
        label=_t('Co Promoter Address Postalcode', 'Co Promoter Address Postalcode'),
        help=_t('postalcode or zip of the co-promoter. It can be empty when not applicable.', 'postalcode or zip of the co-promoter. It can be empty when not applicable.'),
        size=8,
        # source: data.buildingProperty.program.coPromotion.coPromoter.address.postalcode
    ),
    FieldSpec(
        name='x_co_promoter_address_city',
        ttype='char',
        label=_t('Co Promoter Address City', 'Co Promoter Address City'),
        help=_t('city of the co-promoter. It can be empty when not applicable.', 'city of the co-promoter. It can be empty when not applicable.'),
        size=32,
        # source: data.buildingProperty.program.coPromotion.coPromoter.address.city
    ),
    FieldSpec(
        name='x_co_promoter_address_country',
        ttype='char',
        label=_t('Co Promoter Address Country', 'Co Promoter Address Country'),
        help=_t('country where the co-promoter is located. **Note:** You are strongly encouraged to use ISO3166 country codes instead of country names. You can use the three-letter code (alpha-3) which is more closely related to the country name. ISO3166 country codes will be mandatory in the next major version.', 'country where the co-promoter is located. **Note:** You are strongly encouraged to use ISO3166 country codes instead of country names. You can use the three-letter code (alpha-3) which is more closely related to the country name. ISO3166 country codes will be mandatory in the next major version.'),
        size=16,
        # source: data.buildingProperty.program.coPromotion.coPromoter.address.country
    ),
    FieldSpec(
        name='x_co_promoter_url_logo',
        ttype='char',
        label=_t('Co Promoter Url Logo', 'Co Promoter Url Logo'),
        help=_t('URL to the logo of the co-promoter. It can be empty when not applicable.', 'URL to the logo of the co-promoter. It can be empty when not applicable.'),
        size=128,
        # source: data.buildingProperty.program.coPromotion.coPromoter.urlLogo
    ),
)

# ---- conditions (5 fields) ----
DERIVED_CONDITIONS_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_build_state',
        ttype='selection',
        label=_t('Build State', 'Build State'),
        help=_t('What is the current condition of the property? - FIRST_TIME_USE: never been inhabited before - FIRST_TIME_USE_AFTER_REFURBISHMENT: never been inhabited since last refurbishment - MINT_CONDITION: perfect shape - MODERNISED: property architecture has been modernised - REFURBISHED: property is now as new - FULLY_RENOVATED: All the property is renovated - PARTLY_RENOVATED: some parts of the property have been renovated - NEED_OF_RENOVATION: the property needs to be renovated? - WELL_KEPT: good shape. - NEGOTIABLE: the property is not very well kept but it can be used - RIPE_FOR_DEMOLITION: Propert…', 'What is the current condition of the property? - FIRST_TIME_USE: never been inhabited before - FIRST_TIME_USE_AFTER_REFURBISHMENT: never been inhabited since last refurbishment - MINT_CONDITION: perfect shape - MODERNISED: property architecture has been modernised - REFURBISHED: property is now as new - FULLY_RENOVATED: All the property is renovated - PARTLY_RENOVATED: some parts of the property have been renovated - NEED_OF_RENOVATION: the property needs to be renovated? - WELL_KEPT: good shape. - NEGOTIABLE: the property is not very well kept but it can be used - RIPE_FOR_DEMOLITION: Propert…'),
        selection=(
        SelectionOption('FIRST_TIME_USE', _t('First Time Use', 'First Time Use'), 0),
        SelectionOption('FIRST_TIME_USE_AFTER_REFURBISHMENT', _t('First Time Use After Refurbishment', 'First Time Use After Refurbishment'), 1),
        SelectionOption('MINT_CONDITION', _t('Mint Condition', 'Mint Condition'), 2),
        SelectionOption('MODERNISED', _t('Modernised', 'Modernised'), 3),
        SelectionOption('REFURBISHED', _t('Refurbished', 'Refurbished'), 4),
        SelectionOption('FULLY_RENOVATED', _t('Fully Renovated', 'Fully Renovated'), 5),
        SelectionOption('PARTLY_RENOVATED', _t('Partly Renovated', 'Partly Renovated'), 6),
        SelectionOption('NEED_OF_RENOVATION', _t('Need Of Renovation', 'Need Of Renovation'), 7),
        SelectionOption('WELL_KEPT', _t('Well Kept', 'Well Kept'), 8),
        SelectionOption('NEGOTIABLE', _t('Negotiable', 'Negotiable'), 9),
        SelectionOption('RIPE_FOR_DEMOLITION', _t('Ripe For Demolition', 'Ripe For Demolition'), 10),
        SelectionOption('PROJECTED', _t('Projected', 'Projected'), 11),
        SelectionOption('NO_INFORMATION', _t('No Information', 'No Information'), 12),
        SelectionOption('RESTRUCTURED', _t('Restructured', 'Restructured'), 13),
        ),
        # source: data.conditions.buildState
    ),
    FieldSpec(
        name='x_age_state',
        ttype='selection',
        label=_t('Age State', 'Age State'),
        help=_t('the age of the building: OLD is defined as built before 1945. NEW is defined as built within the last 5 years.', 'the age of the building: OLD is defined as built before 1945. NEW is defined as built within the last 5 years.'),
        selection=(
        SelectionOption('OLD', _t('Old', 'Old'), 0),
        SelectionOption('NEW', _t('New', 'New'), 1),
        ),
        # source: data.conditions.ageState
    ),
    FieldSpec(
        name='x_year_of_construction',
        ttype='integer',
        label=_t('Year Of Construction', 'Year Of Construction'),
        help=_t('year of construction', 'year of construction'),
        # source: data.conditions.yearOfConstruction
    ),
    FieldSpec(
        name='x_last_modernisation',
        ttype='integer',
        label=_t('Last Modernisation', 'Last Modernisation'),
        help=_t('last year of modernisation', 'last year of modernisation'),
        # source: data.conditions.lastModernisation
    ),
    FieldSpec(
        name='x_construction_style',
        ttype='selection',
        label=_t('Construction Style', 'Construction Style'),
        help=_t('General construction style of tbe building', 'General construction style of tbe building'),
        selection=(
        SelectionOption('PREFABRICATED', _t('Prefabricated', 'Prefabricated'), 0),
        SelectionOption('SOLID', _t('Solid', 'Solid'), 1),
        SelectionOption('SOLID_PREFABRICATED', _t('Solid Prefabricated', 'Solid Prefabricated'), 2),
        SelectionOption('TIMBERHOUSE', _t('Timberhouse', 'Timberhouse'), 3),
        SelectionOption('WOOD_PREFABRICATED', _t('Wood Prefabricated', 'Wood Prefabricated'), 4),
        SelectionOption('UNSPECIFIED', _t('Unspecified', 'Unspecified'), 5),
        ),
        # source: data.conditions.constructionStyle
    ),
)

# ---- contact (20 fields) ----
DERIVED_CONTACT_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_user_homepage',
        ttype='text',
        label=_t('User Homepage', 'User Homepage'),
        # source: data.contact.userHomepage
    ),
    FieldSpec(
        name='x_main_contact_person_id',
        ttype='text',
        label=_t('Main Contact Person Id', 'Main Contact Person Id'),
        help=_t('ID of main contact person, ID is generated in the Contact Data Controller', 'ID of main contact person, ID is generated in the Contact Data Controller'),
        # source: data.contact.mainContactPersonId
    ),
    FieldSpec(
        name='x_additional_contact_person_id',
        ttype='text',
        label=_t('Additional Contact Person Id', 'Additional Contact Person Id'),
        help=_t('ID of an additional contact person, ID is generated in the Contact Data Controller', 'ID of an additional contact person, ID is generated in the Contact Data Controller'),
        # source: data.contact.additionalContactPersonId
    ),
    FieldSpec(
        name='x_preferred_contact_type',
        ttype='selection',
        label=_t('Preferred Contact Type', 'Preferred Contact Type'),
        help=_t('how the seeker should contact the agency / owner', 'how the seeker should contact the agency / owner'),
        selection=(
        SelectionOption('ANONYMOUS', _t('Anonymous', 'Anonymous'), 0),
        SelectionOption('BY_PHONE', _t('By Phone', 'By Phone'), 1),
        SelectionOption('BY_EMAIL', _t('By Email', 'By Email'), 2),
        SelectionOption('OWN_WEBSITE', _t('Own Website', 'Own Website'), 3),
        ),
        # source: data.contact.preferredContactType
    ),
    FieldSpec(
        name='x_contact_note_en',
        ttype='text',
        label=_t('Contact Note En', 'Contact Note En'),
        # source: data.contact.contactNote.en
    ),
    FieldSpec(
        name='x_contact_note_fr',
        ttype='text',
        label=_t('Contact Note Fr', 'Contact Note Fr'),
        # source: data.contact.contactNote.fr
    ),
    FieldSpec(
        name='x_main_contact_person_name',
        ttype='boolean',
        label=_t('Main Contact Person Name', 'Main Contact Person Name'),
        # source: data.contact.displayedInformation.mainContactPerson.name
    ),
    FieldSpec(
        name='x_main_contact_person_phone',
        ttype='boolean',
        label=_t('Main Contact Person Phone', 'Main Contact Person Phone'),
        # source: data.contact.displayedInformation.mainContactPerson.phone
    ),
    FieldSpec(
        name='x_main_contact_person_mobile_phone',
        ttype='boolean',
        label=_t('Main Contact Person Mobile Phone', 'Main Contact Person Mobile Phone'),
        # source: data.contact.displayedInformation.mainContactPerson.mobilePhone
    ),
    FieldSpec(
        name='x_main_contact_person_email',
        ttype='boolean',
        label=_t('Main Contact Person Email', 'Main Contact Person Email'),
        # source: data.contact.displayedInformation.mainContactPerson.email
    ),
    FieldSpec(
        name='x_main_contact_person_address',
        ttype='boolean',
        label=_t('Main Contact Person Address', 'Main Contact Person Address'),
        # source: data.contact.displayedInformation.mainContactPerson.address
    ),
    FieldSpec(
        name='x_main_contact_person_company_name',
        ttype='boolean',
        label=_t('Main Contact Person Company Name', 'Main Contact Person Company Name'),
        # source: data.contact.displayedInformation.mainContactPerson.companyName
    ),
    FieldSpec(
        name='x_main_contact_person_fax',
        ttype='boolean',
        label=_t('Main Contact Person Fax', 'Main Contact Person Fax'),
        # source: data.contact.displayedInformation.mainContactPerson.fax
    ),
    FieldSpec(
        name='x_additional_contact_person_name',
        ttype='boolean',
        label=_t('Additional Contact Person Name', 'Additional Contact Person Name'),
        # source: data.contact.displayedInformation.additionalContactPerson.name
    ),
    FieldSpec(
        name='x_additional_contact_person_phone',
        ttype='boolean',
        label=_t('Additional Contact Person Phone', 'Additional Contact Person Phone'),
        # source: data.contact.displayedInformation.additionalContactPerson.phone
    ),
    FieldSpec(
        name='x_additional_contact_person_mobile_phone',
        ttype='boolean',
        label=_t('Additional Contact Person Mobile Phone', 'Additional Contact Person Mobile Phone'),
        # source: data.contact.displayedInformation.additionalContactPerson.mobilePhone
    ),
    FieldSpec(
        name='x_additional_contact_person_email',
        ttype='boolean',
        label=_t('Additional Contact Person Email', 'Additional Contact Person Email'),
        # source: data.contact.displayedInformation.additionalContactPerson.email
    ),
    FieldSpec(
        name='x_additional_contact_person_address',
        ttype='boolean',
        label=_t('Additional Contact Person Address', 'Additional Contact Person Address'),
        # source: data.contact.displayedInformation.additionalContactPerson.address
    ),
    FieldSpec(
        name='x_additional_contact_person_company_name',
        ttype='boolean',
        label=_t('Additional Contact Person Company Name', 'Additional Contact Person Company Name'),
        # source: data.contact.displayedInformation.additionalContactPerson.companyName
    ),
    FieldSpec(
        name='x_additional_contact_person_fax',
        ttype='boolean',
        label=_t('Additional Contact Person Fax', 'Additional Contact Person Fax'),
        # source: data.contact.displayedInformation.additionalContactPerson.fax
    ),
)

# ---- country_specific (28 fields) ----
DERIVED_COUNTRY_SPECIFIC_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_is_business_sold',
        ttype='boolean',
        label=_t('Is Business Sold', 'Is Business Sold'),
        help=_t('Is the business run inside the property sold ?', 'Is the business run inside the property sold ?'),
        # source: data.countrySpecific.fr.business.isBusinessSold
    ),
    FieldSpec(
        name='x_business_type',
        ttype='selection',
        label=_t('Business Type', 'Business Type'),
        help=_t('main type of the business', 'main type of the business'),
        selection=(
        SelectionOption('FOOD', _t('Food', 'Food'), 0),
        SelectionOption('TRANSPORT', _t('Transport', 'Transport'), 1),
        SelectionOption('GASTRONOMY_HOTEL', _t('Gastronomy Hotel', 'Gastronomy Hotel'), 2),
        SelectionOption('LOCAL_SHOP', _t('Local Shop', 'Local Shop'), 3),
        SelectionOption('WELLNESS_HEALTHCARE', _t('Wellness Healthcare', 'Wellness Healthcare'), 4),
        SelectionOption('HOUSE_EQUIPMENT', _t('House Equipment', 'House Equipment'), 5),
        SelectionOption('COMPUTER_TELECOM', _t('Computer Telecom', 'Computer Telecom'), 6),
        SelectionOption('LEISURE', _t('Leisure', 'Leisure'), 7),
        SelectionOption('FASHION', _t('Fashion', 'Fashion'), 8),
        SelectionOption('HEALTH', _t('Health', 'Health'), 9),
        SelectionOption('LOCAL', _t('Local', 'Local'), 10),
        ),
        # source: data.countrySpecific.fr.business.businessType
    ),
    FieldSpec(
        name='x_business_sub_type',
        ttype='selection',
        label=_t('Business Sub Type', 'Business Sub Type'),
        help=_t('subtype of the business NOTE WINEWINE entry is deprecated. Use WINE instead.', 'subtype of the business NOTE WINEWINE entry is deprecated. Use WINE instead.'),
        selection=(
        SelectionOption('MEAT_SHOP', _t('Meat Shop', 'Meat Shop'), 0),
        SelectionOption('BAKERY', _t('Bakery', 'Bakery'), 1),
        SelectionOption('CHOCOLATES_CANDIES', _t('Chocolates Candies', 'Chocolates Candies'), 2),
        SelectionOption('GREENGROCERY', _t('Greengrocery', 'Greengrocery'), 3),
        SelectionOption('GROCERY', _t('Grocery', 'Grocery'), 4),
        SelectionOption('DAIRY', _t('Dairy', 'Dairy'), 5),
        SelectionOption('FISH_STORE', _t('Fish Store', 'Fish Store'), 6),
        SelectionOption('CATERING', _t('Catering', 'Catering'), 7),
        SelectionOption('WINE', _t('Wine', 'Wine'), 8),
        SelectionOption('WINEWINE', _t('Winewine', 'Winewine'), 9),
        SelectionOption('MINI_MARKET', _t('Mini Market', 'Mini Market'), 10),
        SelectionOption('SUPERMARKET', _t('Supermarket', 'Supermarket'), 11),
        SelectionOption('DRIVING_SCHOOL', _t('Driving School', 'Driving School'), 12),
        SelectionOption('CAR_MOTORCYCLE_DEALER', _t('Car Motorcycle Dealer', 'Car Motorcycle Dealer'), 13),
        SelectionOption('GARAGE_SERVICE_STATION', _t('Garage Service Station', 'Garage Service Station'), 14),
        SelectionOption('CAFE_BAR_PUB', _t('Cafe Bar Pub', 'Cafe Bar Pub'), 15),
        SelectionOption('CAMPING', _t('Camping', 'Camping'), 16),
        SelectionOption('CREPERIE', _t('Creperie', 'Creperie'), 17),
        SelectionOption('ICECREAM', _t('Icecream', 'Icecream'), 18),
        SelectionOption('HOTEL', _t('Hotel', 'Hotel'), 19),
        SelectionOption('PIZZERIA', _t('Pizzeria', 'Pizzeria'), 20),
        SelectionOption('RESTAURANT', _t('Restaurant', 'Restaurant'), 21),
        SelectionOption('FASTFOOD', _t('Fastfood', 'Fastfood'), 22),
        SelectionOption('TEAROOM', _t('Tearoom', 'Tearoom'), 23),
        SelectionOption('GIFT_SHOP', _t('Gift Shop', 'Gift Shop'), 24),
        SelectionOption('FLORIST', _t('Florist', 'Florist'), 25),
        SelectionOption('HABERDASHERY', _t('Haberdashery', 'Haberdashery'), 26),
        SelectionOption('KIOSK', _t('Kiosk', 'Kiosk'), 27),
        SelectionOption('HAIRDRESSING', _t('Hairdressing', 'Hairdressing'), 28),
        SelectionOption('BEAUTY', _t('Beauty', 'Beauty'), 29),
        SelectionOption('PERFUMERY', _t('Perfumery', 'Perfumery'), 30),
        SelectionOption('FURNISHING', _t('Furnishing', 'Furnishing'), 31),
        SelectionOption('HOUSEHOLD_APPLIANCES', _t('Household Appliances', 'Household Appliances'), 32),
        SelectionOption('COMPUTER_SHOP_OFFICE_SUPPLY', _t('Computer Shop Office Supply', 'Computer Shop Office Supply'), 33),
        SelectionOption('PHONES', _t('Phones', 'Phones'), 34),
        SelectionOption('TRAVEL_AGENCY', _t('Travel Agency', 'Travel Agency'), 35),
        SelectionOption('ARTS_MUSIC', _t('Arts Music', 'Arts Music'), 36),
        SelectionOption('SPORTS_CLUB', _t('Sports Club', 'Sports Club'), 37),
        SelectionOption('CLUB_DISCOTHEQUE', _t('Club Discotheque', 'Club Discotheque'), 38),
        SelectionOption('ARTS_GALLERY', _t('Arts Gallery', 'Arts Gallery'), 39),
        SelectionOption('COMPUTER_SHOP', _t('Computer Shop', 'Computer Shop'), 40),
        SelectionOption('BOOKS', _t('Books', 'Books'), 41),
        SelectionOption('TOYS', _t('Toys', 'Toys'), 42),
        SelectionOption('JEWELLERY', _t('Jewellery', 'Jewellery'), 43),
        SelectionOption('SHOES', _t('Shoes', 'Shoes'), 44),
        SelectionOption('LEATHER', _t('Leather', 'Leather'), 45),
        SelectionOption('CLOTHES', _t('Clothes', 'Clothes'), 46),
        SelectionOption('TAXI_AMBULANCE', _t('Taxi Ambulance', 'Taxi Ambulance'), 47),
        SelectionOption('DENTAL', _t('Dental', 'Dental'), 48),
        SelectionOption('PHYSIOTHERAPIST', _t('Physiotherapist', 'Physiotherapist'), 49),
        SelectionOption('RETIREMENT_HOME', _t('Retirement Home', 'Retirement Home'), 50),
        SelectionOption('OPTIC', _t('Optic', 'Optic'), 51),
        SelectionOption('PHARMACY', _t('Pharmacy', 'Pharmacy'), 52),
        SelectionOption('REAL_ESTATE', _t('Real Estate', 'Real Estate'), 53),
        SelectionOption('PETS', _t('Pets', 'Pets'), 54),
        SelectionOption('DIY', _t('Diy', 'Diy'), 55),
        SelectionOption('SHOE_REPAIR', _t('Shoe Repair', 'Shoe Repair'), 56),
        SelectionOption('RELOCATION', _t('Relocation', 'Relocation'), 57),
        SelectionOption('ELECTRICITY', _t('Electricity', 'Electricity'), 58),
        SelectionOption('GARDENER', _t('Gardener', 'Gardener'), 59),
        SelectionOption('LAUNDROMAT', _t('Laundromat', 'Laundromat'), 60),
        SelectionOption('CARPENTRY', _t('Carpentry', 'Carpentry'), 61),
        SelectionOption('PHOTO', _t('Photo', 'Photo'), 62),
        SelectionOption('PLUMBING_HEATING', _t('Plumbing Heating', 'Plumbing Heating'), 63),
        SelectionOption('LAUNDRY', _t('Laundry', 'Laundry'), 64),
        SelectionOption('LOCKSMITH', _t('Locksmith', 'Locksmith'), 65),
        SelectionOption('GLASSMAKING', _t('Glassmaking', 'Glassmaking'), 66),
        ),
        # source: data.countrySpecific.fr.business.businessSubType
    ),
    FieldSpec(
        name='x_revenue',
        ttype='float',
        label=_t('Revenue', 'Revenue'),
        help=_t('total revenue of the business in the current year', 'total revenue of the business in the current year'),
        # source: data.countrySpecific.fr.business.revenue
    ),
    FieldSpec(
        name='x_revenue_one_year_ago',
        ttype='float',
        label=_t('Revenue One Year Ago', 'Revenue One Year Ago'),
        help=_t('total revenue of the business one year ago', 'total revenue of the business one year ago'),
        # source: data.countrySpecific.fr.business.revenueOneYearAgo
    ),
    FieldSpec(
        name='x_revenue_two_years_ago',
        ttype='float',
        label=_t('Revenue Two Years Ago', 'Revenue Two Years Ago'),
        help=_t('total revenue of the business two years ago', 'total revenue of the business two years ago'),
        # source: data.countrySpecific.fr.business.revenueTwoYearsAgo
    ),
    FieldSpec(
        name='x_revenue_details',
        ttype='text',
        label=_t('Revenue Details', 'Revenue Details'),
        help=_t('additional comment about the revenue of the business', 'additional comment about the revenue of the business'),
        # source: data.countrySpecific.fr.business.revenueDetails
    ),
    FieldSpec(
        name='x_net_income',
        ttype='float',
        label=_t('Net Income', 'Net Income'),
        help=_t('net income of the business in the current year', 'net income of the business in the current year'),
        # source: data.countrySpecific.fr.business.netIncome
    ),
    FieldSpec(
        name='x_net_income_one_year_ago',
        ttype='float',
        label=_t('Net Income One Year Ago', 'Net Income One Year Ago'),
        help=_t('net income of the business one year ago', 'net income of the business one year ago'),
        # source: data.countrySpecific.fr.business.netIncomeOneYearAgo
    ),
    FieldSpec(
        name='x_net_income_two_years_ago',
        ttype='float',
        label=_t('Net Income Two Years Ago', 'Net Income Two Years Ago'),
        help=_t('net income of the business two years ago', 'net income of the business two years ago'),
        # source: data.countrySpecific.fr.business.netIncomeTwoYearsAgo
    ),
    FieldSpec(
        name='x_is_part_of_network',
        ttype='boolean',
        label=_t('Is Part Of Network', 'Is Part Of Network'),
        help=_t('the business is part of a bigger network', 'the business is part of a bigger network'),
        # source: data.countrySpecific.fr.business.isPartOfNetwork
    ),
    FieldSpec(
        name='x_down_payment',
        ttype='float',
        label=_t('Down Payment', 'Down Payment'),
        help=_t('down payment for the purchase of the business in euros.', 'down payment for the purchase of the business in euros.'),
        # source: data.countrySpecific.fr.business.downPayment
    ),
    FieldSpec(
        name='x_is_no_nuisance',
        ttype='boolean',
        label=_t('Is No Nuisance', 'Is No Nuisance'),
        help=_t('the business must not inconvenience neighbours', 'the business must not inconvenience neighbours'),
        # source: data.countrySpecific.fr.business.isNoNuisance
    ),
    FieldSpec(
        name='x_is_divisible',
        ttype='boolean',
        label=_t('Is Divisible', 'Is Divisible'),
        help=_t('parts of the business can be sold or rent. parts can be listed or not.', 'parts of the business can be sold or rent. parts can be listed or not.'),
        # source: data.countrySpecific.fr.business.isDivisible
    ),
    FieldSpec(
        name='x_currency',
        ttype='selection',
        label=_t('Currency', 'Currency'),
        help=_t('the currency must be entered as ISO 4217 currency code. Please refer to https://www.iso.org/iso-4217-currency-codes.html Last checked: October 1st, 2021 Here are the alphabetic three-letter country codes: - AED: UAE Dirham - AFN: Afghani - ALL: Lek - AMD: Armenian Dram - ANG: Netherlands Antillean Guilder - AOA: Kwanza - ARS: Argentine Peso - AUD: Australian Dollar - AWG: Aruban Florin - AZN: Azerbaijan Manat - BAM: Convertible Mark - BBD: Barbados Dollar - BDT: Taka - BGN: Bulgarian Lev - BHD: Bahraini Dinar - BIF: Burundi Franc - BMD: Bermudian Dollar - BND: Brunei Dollar - BOB: Boliviano -…', 'the currency must be entered as ISO 4217 currency code. Please refer to https://www.iso.org/iso-4217-currency-codes.html Last checked: October 1st, 2021 Here are the alphabetic three-letter country codes: - AED: UAE Dirham - AFN: Afghani - ALL: Lek - AMD: Armenian Dram - ANG: Netherlands Antillean Guilder - AOA: Kwanza - ARS: Argentine Peso - AUD: Australian Dollar - AWG: Aruban Florin - AZN: Azerbaijan Manat - BAM: Convertible Mark - BBD: Barbados Dollar - BDT: Taka - BGN: Bulgarian Lev - BHD: Bahraini Dinar - BIF: Burundi Franc - BMD: Bermudian Dollar - BND: Brunei Dollar - BOB: Boliviano -…'),
        selection=(
        SelectionOption('AED', _t('Aed', 'Aed'), 0),
        SelectionOption('AFN', _t('Afn', 'Afn'), 1),
        SelectionOption('ALL', _t('All', 'All'), 2),
        SelectionOption('AMD', _t('Amd', 'Amd'), 3),
        SelectionOption('ANG', _t('Ang', 'Ang'), 4),
        SelectionOption('AOA', _t('Aoa', 'Aoa'), 5),
        SelectionOption('ARS', _t('Ars', 'Ars'), 6),
        SelectionOption('AUD', _t('Aud', 'Aud'), 7),
        SelectionOption('AWG', _t('Awg', 'Awg'), 8),
        SelectionOption('AZN', _t('Azn', 'Azn'), 9),
        SelectionOption('BAM', _t('Bam', 'Bam'), 10),
        SelectionOption('BBD', _t('Bbd', 'Bbd'), 11),
        SelectionOption('BDT', _t('Bdt', 'Bdt'), 12),
        SelectionOption('BGN', _t('Bgn', 'Bgn'), 13),
        SelectionOption('BHD', _t('Bhd', 'Bhd'), 14),
        SelectionOption('BIF', _t('Bif', 'Bif'), 15),
        SelectionOption('BMD', _t('Bmd', 'Bmd'), 16),
        SelectionOption('BND', _t('Bnd', 'Bnd'), 17),
        SelectionOption('BOB', _t('Bob', 'Bob'), 18),
        SelectionOption('BOV', _t('Bov', 'Bov'), 19),
        SelectionOption('BRL', _t('Brl', 'Brl'), 20),
        SelectionOption('BSD', _t('Bsd', 'Bsd'), 21),
        SelectionOption('BTN', _t('Btn', 'Btn'), 22),
        SelectionOption('BWP', _t('Bwp', 'Bwp'), 23),
        SelectionOption('BYN', _t('Byn', 'Byn'), 24),
        SelectionOption('BZD', _t('Bzd', 'Bzd'), 25),
        SelectionOption('CAD', _t('Cad', 'Cad'), 26),
        SelectionOption('CDF', _t('Cdf', 'Cdf'), 27),
        SelectionOption('CHE', _t('Che', 'Che'), 28),
        SelectionOption('CHF', _t('Chf', 'Chf'), 29),
        SelectionOption('CHW', _t('Chw', 'Chw'), 30),
        SelectionOption('CLF', _t('Clf', 'Clf'), 31),
        SelectionOption('CLP', _t('Clp', 'Clp'), 32),
        SelectionOption('CNY', _t('Cny', 'Cny'), 33),
        SelectionOption('COP', _t('Cop', 'Cop'), 34),
        SelectionOption('COU', _t('Cou', 'Cou'), 35),
        SelectionOption('CRC', _t('Crc', 'Crc'), 36),
        SelectionOption('CUC', _t('Cuc', 'Cuc'), 37),
        SelectionOption('CUP', _t('Cup', 'Cup'), 38),
        SelectionOption('CVE', _t('Cve', 'Cve'), 39),
        SelectionOption('CZK', _t('Czk', 'Czk'), 40),
        SelectionOption('DJF', _t('Djf', 'Djf'), 41),
        SelectionOption('DKK', _t('Dkk', 'Dkk'), 42),
        SelectionOption('DOP', _t('Dop', 'Dop'), 43),
        SelectionOption('DZD', _t('Dzd', 'Dzd'), 44),
        SelectionOption('EGP', _t('Egp', 'Egp'), 45),
        SelectionOption('ERN', _t('Ern', 'Ern'), 46),
        SelectionOption('ETB', _t('Etb', 'Etb'), 47),
        SelectionOption('EUR', _t('Eur', 'Eur'), 48),
        SelectionOption('FJD', _t('Fjd', 'Fjd'), 49),
        SelectionOption('FKP', _t('Fkp', 'Fkp'), 50),
        SelectionOption('GBP', _t('Gbp', 'Gbp'), 51),
        SelectionOption('GEL', _t('Gel', 'Gel'), 52),
        SelectionOption('GHS', _t('Ghs', 'Ghs'), 53),
        SelectionOption('GIP', _t('Gip', 'Gip'), 54),
        SelectionOption('GMD', _t('Gmd', 'Gmd'), 55),
        SelectionOption('GNF', _t('Gnf', 'Gnf'), 56),
        SelectionOption('GTQ', _t('Gtq', 'Gtq'), 57),
        SelectionOption('GYD', _t('Gyd', 'Gyd'), 58),
        SelectionOption('HKD', _t('Hkd', 'Hkd'), 59),
        SelectionOption('HNL', _t('Hnl', 'Hnl'), 60),
        SelectionOption('HRK', _t('Hrk', 'Hrk'), 61),
        SelectionOption('HTG', _t('Htg', 'Htg'), 62),
        SelectionOption('HUF', _t('Huf', 'Huf'), 63),
        SelectionOption('IDR', _t('Idr', 'Idr'), 64),
        SelectionOption('ILS', _t('Ils', 'Ils'), 65),
        SelectionOption('INR', _t('Inr', 'Inr'), 66),
        SelectionOption('IQD', _t('Iqd', 'Iqd'), 67),
        SelectionOption('IRR', _t('Irr', 'Irr'), 68),
        SelectionOption('ISK', _t('Isk', 'Isk'), 69),
        SelectionOption('JMD', _t('Jmd', 'Jmd'), 70),
        SelectionOption('JOD', _t('Jod', 'Jod'), 71),
        SelectionOption('JPY', _t('Jpy', 'Jpy'), 72),
        SelectionOption('KES', _t('Kes', 'Kes'), 73),
        SelectionOption('KGS', _t('Kgs', 'Kgs'), 74),
        SelectionOption('KHR', _t('Khr', 'Khr'), 75),
        SelectionOption('KMF', _t('Kmf', 'Kmf'), 76),
        SelectionOption('KPW', _t('Kpw', 'Kpw'), 77),
        SelectionOption('KRW', _t('Krw', 'Krw'), 78),
        SelectionOption('KWD', _t('Kwd', 'Kwd'), 79),
        SelectionOption('KYD', _t('Kyd', 'Kyd'), 80),
        SelectionOption('KZT', _t('Kzt', 'Kzt'), 81),
        SelectionOption('LAK', _t('Lak', 'Lak'), 82),
        SelectionOption('LBP', _t('Lbp', 'Lbp'), 83),
        SelectionOption('LKR', _t('Lkr', 'Lkr'), 84),
        SelectionOption('LRD', _t('Lrd', 'Lrd'), 85),
        SelectionOption('LSL', _t('Lsl', 'Lsl'), 86),
        SelectionOption('LYD', _t('Lyd', 'Lyd'), 87),
        SelectionOption('MAD', _t('Mad', 'Mad'), 88),
        SelectionOption('MDL', _t('Mdl', 'Mdl'), 89),
        SelectionOption('MGA', _t('Mga', 'Mga'), 90),
        SelectionOption('MKD', _t('Mkd', 'Mkd'), 91),
        SelectionOption('MMK', _t('Mmk', 'Mmk'), 92),
        SelectionOption('MNT', _t('Mnt', 'Mnt'), 93),
        SelectionOption('MOP', _t('Mop', 'Mop'), 94),
        SelectionOption('MRU', _t('Mru', 'Mru'), 95),
        SelectionOption('MUR', _t('Mur', 'Mur'), 96),
        SelectionOption('MVR', _t('Mvr', 'Mvr'), 97),
        SelectionOption('MWK', _t('Mwk', 'Mwk'), 98),
        SelectionOption('MXN', _t('Mxn', 'Mxn'), 99),
        SelectionOption('MXV', _t('Mxv', 'Mxv'), 100),
        SelectionOption('MYR', _t('Myr', 'Myr'), 101),
        SelectionOption('MZN', _t('Mzn', 'Mzn'), 102),
        SelectionOption('NAD', _t('Nad', 'Nad'), 103),
        SelectionOption('NGN', _t('Ngn', 'Ngn'), 104),
        SelectionOption('NIO', _t('Nio', 'Nio'), 105),
        SelectionOption('NOK', _t('Nok', 'Nok'), 106),
        SelectionOption('NPR', _t('Npr', 'Npr'), 107),
        SelectionOption('NZD', _t('Nzd', 'Nzd'), 108),
        SelectionOption('OMR', _t('Omr', 'Omr'), 109),
        SelectionOption('PAB', _t('Pab', 'Pab'), 110),
        SelectionOption('PEN', _t('Pen', 'Pen'), 111),
        SelectionOption('PGK', _t('Pgk', 'Pgk'), 112),
        SelectionOption('PHP', _t('Php', 'Php'), 113),
        SelectionOption('PKR', _t('Pkr', 'Pkr'), 114),
        SelectionOption('PLN', _t('Pln', 'Pln'), 115),
        SelectionOption('PYG', _t('Pyg', 'Pyg'), 116),
        SelectionOption('QAR', _t('Qar', 'Qar'), 117),
        SelectionOption('RON', _t('Ron', 'Ron'), 118),
        SelectionOption('RSD', _t('Rsd', 'Rsd'), 119),
        SelectionOption('RUB', _t('Rub', 'Rub'), 120),
        SelectionOption('RWF', _t('Rwf', 'Rwf'), 121),
        SelectionOption('SAR', _t('Sar', 'Sar'), 122),
        SelectionOption('SBD', _t('Sbd', 'Sbd'), 123),
        SelectionOption('SCR', _t('Scr', 'Scr'), 124),
        SelectionOption('SDG', _t('Sdg', 'Sdg'), 125),
        SelectionOption('SEK', _t('Sek', 'Sek'), 126),
        SelectionOption('SGD', _t('Sgd', 'Sgd'), 127),
        SelectionOption('SHP', _t('Shp', 'Shp'), 128),
        SelectionOption('SLL', _t('Sll', 'Sll'), 129),
        SelectionOption('SOS', _t('Sos', 'Sos'), 130),
        SelectionOption('SRD', _t('Srd', 'Srd'), 131),
        SelectionOption('SSP', _t('Ssp', 'Ssp'), 132),
        SelectionOption('STN', _t('Stn', 'Stn'), 133),
        SelectionOption('SVC', _t('Svc', 'Svc'), 134),
        SelectionOption('SYP', _t('Syp', 'Syp'), 135),
        SelectionOption('SZL', _t('Szl', 'Szl'), 136),
        SelectionOption('THB', _t('Thb', 'Thb'), 137),
        SelectionOption('TJS', _t('Tjs', 'Tjs'), 138),
        SelectionOption('TMT', _t('Tmt', 'Tmt'), 139),
        SelectionOption('TND', _t('Tnd', 'Tnd'), 140),
        SelectionOption('TOP', _t('Top', 'Top'), 141),
        SelectionOption('TRY', _t('Try', 'Try'), 142),
        SelectionOption('TTD', _t('Ttd', 'Ttd'), 143),
        SelectionOption('TWD', _t('Twd', 'Twd'), 144),
        SelectionOption('TZS', _t('Tzs', 'Tzs'), 145),
        SelectionOption('UAH', _t('Uah', 'Uah'), 146),
        SelectionOption('UGX', _t('Ugx', 'Ugx'), 147),
        SelectionOption('USD', _t('Usd', 'Usd'), 148),
        SelectionOption('USN', _t('Usn', 'Usn'), 149),
        SelectionOption('UYI', _t('Uyi', 'Uyi'), 150),
        SelectionOption('UYU', _t('Uyu', 'Uyu'), 151),
        SelectionOption('UYW', _t('Uyw', 'Uyw'), 152),
        SelectionOption('UZS', _t('Uzs', 'Uzs'), 153),
        SelectionOption('VED', _t('Ved', 'Ved'), 154),
        SelectionOption('VES', _t('Ves', 'Ves'), 155),
        SelectionOption('VND', _t('Vnd', 'Vnd'), 156),
        SelectionOption('VUV', _t('Vuv', 'Vuv'), 157),
        SelectionOption('WST', _t('Wst', 'Wst'), 158),
        SelectionOption('XAF', _t('Xaf', 'Xaf'), 159),
        SelectionOption('XAG', _t('Xag', 'Xag'), 160),
        SelectionOption('XAU', _t('Xau', 'Xau'), 161),
        SelectionOption('XBA', _t('Xba', 'Xba'), 162),
        SelectionOption('XBB', _t('Xbb', 'Xbb'), 163),
        SelectionOption('XBC', _t('Xbc', 'Xbc'), 164),
        SelectionOption('XBD', _t('Xbd', 'Xbd'), 165),
        SelectionOption('XCD', _t('Xcd', 'Xcd'), 166),
        SelectionOption('XDR', _t('Xdr', 'Xdr'), 167),
        SelectionOption('XOF', _t('Xof', 'Xof'), 168),
        SelectionOption('XPD', _t('Xpd', 'Xpd'), 169),
        SelectionOption('XPF', _t('Xpf', 'Xpf'), 170),
        SelectionOption('XPT', _t('Xpt', 'Xpt'), 171),
        SelectionOption('XSU', _t('Xsu', 'Xsu'), 172),
        SelectionOption('XTS', _t('Xts', 'Xts'), 173),
        SelectionOption('XUA', _t('Xua', 'Xua'), 174),
        SelectionOption('XXX', _t('Xxx', 'Xxx'), 175),
        SelectionOption('YER', _t('Yer', 'Yer'), 176),
        SelectionOption('ZAR', _t('Zar', 'Zar'), 177),
        SelectionOption('ZMW', _t('Zmw', 'Zmw'), 178),
        SelectionOption('ZWL', _t('Zwl', 'Zwl'), 179),
        ),
        # source: data.countrySpecific.fr.subdivisions.currency
    ),
    FieldSpec(
        name='x_mandate_number',
        ttype='char',
        label=_t('Mandate Number', 'Mandate Number'),
        help=_t('estate agent mandate number', 'estate agent mandate number'),
        # source: data.countrySpecific.fr.agentMandate.mandateNumber
    ),
    FieldSpec(
        name='x_mandate_type',
        ttype='selection',
        label=_t('Mandate Type', 'Mandate Type'),
        help=_t('estate agent mandate type', 'estate agent mandate type'),
        selection=(
        SelectionOption('SIMPLE', _t('Simple', 'Simple'), 0),
        SelectionOption('EXCLUSIVE', _t('Exclusive', 'Exclusive'), 1),
        ),
        # source: data.countrySpecific.fr.agentMandate.mandateType
    ),
    FieldSpec(
        name='x_agent_mandate_start_date',
        ttype='date',
        label=_t('Agent Mandate Start Date', 'Agent Mandate Start Date'),
        help=_t('estate agent mandate start date (ISO 8601 formatted)', 'estate agent mandate start date (ISO 8601 formatted)'),
        # source: data.countrySpecific.fr.agentMandate.startDate
    ),
    FieldSpec(
        name='x_agent_mandate_end_date',
        ttype='date',
        label=_t('Agent Mandate End Date', 'Agent Mandate End Date'),
        help=_t('estate agent mandate end ISO 8601 formatted date', 'estate agent mandate end ISO 8601 formatted date'),
        # source: data.countrySpecific.fr.agentMandate.endDate
    ),
    FieldSpec(
        name='x_mandate_co_owner_id1',
        ttype='char',
        label=_t('Mandate Co Owner Id1', 'Mandate Co Owner Id1'),
        help=_t('1st estate agent mandate co-owner ID', '1st estate agent mandate co-owner ID'),
        # source: data.countrySpecific.fr.agentMandate.mandateCoOwnerId1
    ),
    FieldSpec(
        name='x_mandate_co_owner_id2',
        ttype='char',
        label=_t('Mandate Co Owner Id2', 'Mandate Co Owner Id2'),
        help=_t('2nd estate agent mandate co-owner ID', '2nd estate agent mandate co-owner ID'),
        # source: data.countrySpecific.fr.agentMandate.mandateCoOwnerId2
    ),
    FieldSpec(
        name='x_mandate_co_owner_id3',
        ttype='char',
        label=_t('Mandate Co Owner Id3', 'Mandate Co Owner Id3'),
        help=_t('3rd estate agent mandate co-owner ID', '3rd estate agent mandate co-owner ID'),
        # source: data.countrySpecific.fr.agentMandate.mandateCoOwnerId3
    ),
    FieldSpec(
        name='x_is_polluting',
        ttype='boolean',
        label=_t('Is Polluting', 'Is Polluting'),
        help=_t('indicates if the property generates pollution', 'indicates if the property generates pollution'),
        # source: data.countrySpecific.fr.risk.isPolluting
    ),
    FieldSpec(
        name='x_date_of_statement_of_risks_and_pollution',
        ttype='date',
        label=_t('Date Of Statement Of Risks And Pollution', 'Date Of Statement Of Risks And Pollution'),
        help=_t('date of Establishment statement of Risks and Pollution', 'date of Establishment statement of Risks and Pollution'),
        # source: data.countrySpecific.fr.risk.dateOfStatementOfRisksAndPollution
    ),
    FieldSpec(
        name='x_special_offer_start_date',
        ttype='date',
        label=_t('Special Offer Start Date', 'Special Offer Start Date'),
        help=_t('start date of the special offer', 'start date of the special offer'),
        # source: data.countrySpecific.fr.commercial.specialOffer.startDate
    ),
    FieldSpec(
        name='x_special_offer_end_date',
        ttype='date',
        label=_t('Special Offer End Date', 'Special Offer End Date'),
        help=_t('end date of the special offer', 'end date of the special offer'),
        # source: data.countrySpecific.fr.commercial.specialOffer.endDate
    ),
    FieldSpec(
        name='x_commercial_text',
        ttype='text',
        label=_t('Commercial Text', 'Commercial Text'),
        help=_t('commercial text for the special offer', 'commercial text for the special offer'),
        # source: data.countrySpecific.fr.commercial.specialOffer.commercialText
    ),
    FieldSpec(
        name='x_legal_notice',
        ttype='text',
        label=_t('Legal Notice', 'Legal Notice'),
        help=_t('legal notes for the special offer', 'legal notes for the special offer'),
        # source: data.countrySpecific.fr.commercial.specialOffer.legalNotice
    ),
)

# ---- distribution_type (1 fields) ----
DERIVED_DISTRIBUTION_TYPE_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_distribution_type',
        ttype='selection',
        label=_t('Distribution Type', 'Type de distribution'),
        help=_t('the distribution type of the property. - BUY: regular type of property for sale - RENT: regular type of property for rent - COMPULSORY_AUCTION: auction ordered by the courts - BUY_AUCTION: bids for the property can be submitted within a limited time period. The seller can accept, reject or negotiate the bid. Most important difference to a classic auction: the highest bid does not necessarily have to win. de: Bieterverfahren', 'the distribution type of the property. - BUY: regular type of property for sale - RENT: regular type of property for rent - COMPULSORY_AUCTION: auction ordered by the courts - BUY_AUCTION: bids for the property can be submitted within a limited time period. The seller can accept, reject or negotiate the bid. Most important difference to a classic auction: the highest bid does not necessarily have to win. de: Bieterverfahren'),
        selection=(
        SelectionOption('BUY', _t('Buy', 'Buy'), 0),
        SelectionOption('RENT', _t('Rent', 'Rent'), 1),
        SelectionOption('COMPULSORY_AUCTION', _t('Compulsory Auction', 'Compulsory Auction'), 2),
        SelectionOption('BUY_AUCTION', _t('Buy Auction', 'Buy Auction'), 3),
        ),
        # source: data.distributionType
    ),
)

# ---- energy (35 fields) ----
DERIVED_ENERGY_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_heat_method',
        ttype='selection',
        label=_t('Heat Method', 'Heat Method'),
        help=_t('heating method, per storey/floor or central in building.', 'heating method, per storey/floor or central in building.'),
        selection=(
        SelectionOption('CENTRAL', _t('Central', 'Central'), 0),
        SelectionOption('INDIVIDUAL', _t('Individual', 'Individual'), 1),
        SelectionOption('STOREY', _t('Storey', 'Storey'), 2),
        ),
        # source: data.energy.energyType.heatMethod
    ),
    FieldSpec(
        name='x_air',
        ttype='boolean',
        label=_t('Air', 'Air'),
        help=_t('(warm) air heater does not use a medium to store its heat. Air is sucked in, heated and directly passed on to the rooms to be heated. fr: aerotherme', '(warm) air heater does not use a medium to store its heat. Air is sucked in, heated and directly passed on to the rooms to be heated. fr: aerotherme'),
        # source: data.energy.energyType.heatForm.air
    ),
    FieldSpec(
        name='x_radiator',
        ttype='boolean',
        label=_t('Radiator', 'Radiator'),
        help=_t('radiators are connected to heating circuit through which hot water flows to distribute the heat in the rooms.', 'radiators are connected to heating circuit through which hot water flows to distribute the heat in the rooms.'),
        # source: data.energy.energyType.heatForm.radiator
    ),
    FieldSpec(
        name='x_stove',
        ttype='boolean',
        label=_t('Stove', 'Stove'),
        help=_t('stove that can be fired with wood, oil, coal', 'stove that can be fired with wood, oil, coal'),
        # source: data.energy.energyType.heatForm.stove
    ),
    FieldSpec(
        name='x_underfloor',
        ttype='boolean',
        label=_t('Underfloor', 'Underfloor'),
        help=_t('pipes are laid in the floor through which warm water flows and heats the floor and thus also the rooms.', 'pipes are laid in the floor through which warm water flows and heats the floor and thus also the rooms.'),
        # source: data.energy.energyType.heatForm.underfloor
    ),
    FieldSpec(
        name='x_wall_ceiling',
        ttype='boolean',
        label=_t('Wall Ceiling', 'Wall Ceiling'),
        help=_t('heating elements are mounted on the wall or ceiling', 'heating elements are mounted on the wall or ceiling'),
        # source: data.energy.energyType.heatForm.wallCeiling
    ),
    FieldSpec(
        name='x_coal',
        ttype='boolean',
        label=_t('Coal', 'Coal'),
        # source: data.energy.energyType.energySource.coal
    ),
    FieldSpec(
        name='x_energy_source_district_heating',
        ttype='boolean',
        label=_t('Energy Source District Heating', 'Energy Source District Heating'),
        help=_t('system for distributing heat generated in a centralized location', 'system for distributing heat generated in a centralized location'),
        # source: data.energy.energyType.energySource.districtHeating
    ),
    FieldSpec(
        name='x_energy_source_electric',
        ttype='boolean',
        label=_t('Energy Source Electric', 'Energy Source Electric'),
        # source: data.energy.energyType.energySource.electric
    ),
    FieldSpec(
        name='x_energy_source_gas',
        ttype='boolean',
        label=_t('Energy Source Gas', 'Energy Source Gas'),
        # source: data.energy.energyType.energySource.gas
    ),
    FieldSpec(
        name='x_geothermal',
        ttype='boolean',
        label=_t('Geothermal', 'Geothermal'),
        help=_t('thermal energy from within the earth', 'thermal energy from within the earth'),
        # source: data.energy.energyType.energySource.geothermal
    ),
    FieldSpec(
        name='x_liquid_gas',
        ttype='boolean',
        label=_t('Liquid Gas', 'Liquid Gas'),
        # source: data.energy.energyType.energySource.liquidGas
    ),
    FieldSpec(
        name='x_oil',
        ttype='boolean',
        label=_t('Oil', 'Oil'),
        # source: data.energy.energyType.energySource.oil
    ),
    FieldSpec(
        name='x_solar_heat',
        ttype='boolean',
        label=_t('Solar Heat', 'Solar Heat'),
        # source: data.energy.energyType.energySource.solarHeat
    ),
    FieldSpec(
        name='x_solar_power',
        ttype='boolean',
        label=_t('Solar Power', 'Solar Power'),
        # source: data.energy.energyType.energySource.solarPower
    ),
    FieldSpec(
        name='x_wind',
        ttype='boolean',
        label=_t('Wind', 'Wind'),
        # source: data.energy.energyType.energySource.wind
    ),
    FieldSpec(
        name='x_wood',
        ttype='boolean',
        label=_t('Wood', 'Wood'),
        # source: data.energy.energyType.energySource.wood
    ),
    FieldSpec(
        name='x_wood_pellet',
        ttype='boolean',
        label=_t('Wood Pellet', 'Wood Pellet'),
        # source: data.energy.energyType.energySource.woodPellet
    ),
    FieldSpec(
        name='x_fossilburning',
        ttype='boolean',
        label=_t('Fossilburning', 'Fossilburning'),
        # source: data.energy.energyType.energyGeneration.fossilburning
    ),
    FieldSpec(
        name='x_heatpump',
        ttype='boolean',
        label=_t('Heatpump', 'Heatpump'),
        # source: data.energy.energyType.energyGeneration.heatpump
    ),
    FieldSpec(
        name='x_combined_heat_and_power_plant',
        ttype='boolean',
        label=_t('Combined Heat And Power Plant', 'Combined Heat And Power Plant'),
        # source: data.energy.energyType.energyGeneration.combinedHeatAndPowerPlant
    ),
    FieldSpec(
        name='x_max_electrical_power',
        ttype='integer',
        label=_t('Max Electrical Power', 'Max Electrical Power'),
        help=_t('maximum electric power available for the property, expressed in kVA', 'maximum electric power available for the property, expressed in kVA'),
        # source: data.energy.energyType.maxElectricalPower
    ),
    FieldSpec(
        name='x_certificate_type',
        ttype='selection',
        label=_t('Certificate Type', 'Certificate Type'),
        help=_t("Version of the certificate: - DPE_V01_2011: 1st version of the certificate, can be displayed until end of 2022 - DPE_V07_2021: last known version of the certificate today. Available since June, 2021 - NOT_APPLICABLE: this property should not have an energy certificate or it has been exempted - EMPTY: empty certificate. Only allowed on v01. Any professional could not write the certificate. sometimes technically not even possible. fr: 'DPE Vierge'.", "Version of the certificate: - DPE_V01_2011: 1st version of the certificate, can be displayed until end of 2022 - DPE_V07_2021: last known version of the certificate today. Available since June, 2021 - NOT_APPLICABLE: this property should not have an energy certificate or it has been exempted - EMPTY: empty certificate. Only allowed on v01. Any professional could not write the certificate. sometimes technically not even possible. fr: 'DPE Vierge'."),
        selection=(
        SelectionOption('DPE_V01_2011', _t('Dpe V01 2011', 'Dpe V01 2011'), 0),
        SelectionOption('DPE_V07_2021', _t('Dpe V07 2021', 'Dpe V07 2021'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        SelectionOption('EMPTY', _t('Empty', 'Empty'), 3),
        ),
        # source: data.energy.countrySpecific.fr.energyCertificate.certificateType
    ),
    FieldSpec(
        name='x_overall_energy_need',
        ttype='float',
        label=_t('Overall Energy Need', 'Overall Energy Need'),
        help=_t('DPE: Energy Value in KWhEP/m2/year', 'DPE: Energy Value in KWhEP/m2/year'),
        # source: data.energy.countrySpecific.fr.energyCertificate.overallEnergyNeed
    ),
    FieldSpec(
        name='x_efficiency_class',
        ttype='selection',
        label=_t('Efficiency Class', 'Efficiency Class'),
        help=_t('Energy Letter according to the French Regulations', 'Energy Letter according to the French Regulations'),
        selection=(
        SelectionOption('A', _t('A', 'A'), 0),
        SelectionOption('B', _t('B', 'B'), 1),
        SelectionOption('C', _t('C', 'C'), 2),
        SelectionOption('D', _t('D', 'D'), 3),
        SelectionOption('E', _t('E', 'E'), 4),
        SelectionOption('F', _t('F', 'F'), 5),
        SelectionOption('G', _t('G', 'G'), 6),
        ),
        # source: data.energy.countrySpecific.fr.energyCertificate.efficiencyClass
    ),
    FieldSpec(
        name='x_g_h_g_emission',
        ttype='float',
        label=_t('G H G Emission', 'G H G Emission'),
        help=_t('GreenHouse Gas emissions in KgCO2/m²/year', 'GreenHouse Gas emissions in KgCO2/m²/year'),
        # source: data.energy.countrySpecific.fr.energyCertificate.GHGEmission
    ),
    FieldSpec(
        name='x_g_h_g_emission_class',
        ttype='selection',
        label=_t('G H G Emission Class', 'G H G Emission Class'),
        help=_t('GreenHouse Gas emission Letter according to the French Regulations', 'GreenHouse Gas emission Letter according to the French Regulations'),
        selection=(
        SelectionOption('A', _t('A', 'A'), 0),
        SelectionOption('B', _t('B', 'B'), 1),
        SelectionOption('C', _t('C', 'C'), 2),
        SelectionOption('D', _t('D', 'D'), 3),
        SelectionOption('E', _t('E', 'E'), 4),
        SelectionOption('F', _t('F', 'F'), 5),
        SelectionOption('G', _t('G', 'G'), 6),
        ),
        # source: data.energy.countrySpecific.fr.energyCertificate.GHGEmissionClass
    ),
    FieldSpec(
        name='x_release_date',
        ttype='date',
        label=_t('Release Date', 'Release Date'),
        help=_t('release date of the certificate. The date is an ISO 8601 formatted string', 'release date of the certificate. The date is an ISO 8601 formatted string'),
        # source: data.energy.countrySpecific.fr.energyCertificate.releaseDate
    ),
    FieldSpec(
        name='x_energy_consumption_cost_min',
        ttype='float',
        label=_t('Energy Consumption Cost Min', 'Energy Consumption Cost Min'),
        help=_t('Estimation of Min energy consumption of the property. in €/year.', 'Estimation of Min energy consumption of the property. in €/year.'),
        # source: data.energy.countrySpecific.fr.energyCertificate.energyConsumptionCostMin
    ),
    FieldSpec(
        name='x_energy_consumption_cost_max',
        ttype='float',
        label=_t('Energy Consumption Cost Max', 'Energy Consumption Cost Max'),
        help=_t('Estimation of Max energy consumption of the property. in €/year.', 'Estimation of Max energy consumption of the property. in €/year.'),
        # source: data.energy.countrySpecific.fr.energyCertificate.energyConsumptionCostMax
    ),
    FieldSpec(
        name='x_year_of_consumption_cost_estimation',
        ttype='integer',
        label=_t('Year Of Consumption Cost Estimation', 'Year Of Consumption Cost Estimation'),
        help=_t("Year during which the min/max consumption estimation (based on year's bills) is based on", "Year during which the min/max consumption estimation (based on year's bills) is based on"),
        # source: data.energy.countrySpecific.fr.energyCertificate.yearOfConsumptionCostEstimation
    ),
    FieldSpec(
        name='x_date_of_consumption_cost_estimation',
        ttype='date',
        label=_t('Date Of Consumption Cost Estimation', 'Date Of Consumption Cost Estimation'),
        help=_t("Date on which the min/max consumption estimation (based on year's bills) is based on", "Date on which the min/max consumption estimation (based on year's bills) is based on"),
        # source: data.energy.countrySpecific.fr.energyCertificate.dateOfConsumptionCostEstimation
    ),
    FieldSpec(
        name='x_final_consumption',
        ttype='integer',
        label=_t('Final Consumption', 'Final Consumption'),
        help=_t('The energy consumption of the property, measured in KWh/m2/an.', 'The energy consumption of the property, measured in KWh/m2/an.'),
        # source: data.energy.countrySpecific.fr.energyCertificate.finalConsumption
    ),
    FieldSpec(
        name='x_tarification_e_d_f',
        ttype='selection',
        label=_t('Tarification E D F', 'Tarification E D F'),
        help=_t('Type de tarification EDF', 'Type de tarification EDF'),
        selection=(
        SelectionOption('BLEU', _t('Bleu', 'Bleu'), 0),
        SelectionOption('JAUNE', _t('Jaune', 'Jaune'), 1),
        SelectionOption('VERT', _t('Vert', 'Vert'), 2),
        ),
        # source: data.energy.countrySpecific.fr.tarificationEDF
    ),
    FieldSpec(
        name='x_house_energy_standard_type',
        ttype='selection',
        label=_t('House Energy Standard Type', 'House Energy Standard Type'),
        help=_t('Energy standard to which the property is compliant', 'Energy standard to which the property is compliant'),
        selection=(
        SelectionOption('RT2012', _t('Rt2012', 'Rt2012'), 0),
        SelectionOption('RT2020', _t('Rt2020', 'Rt2020'), 1),
        SelectionOption('HIGH_PERFORMANCE', _t('High Performance', 'High Performance'), 2),
        SelectionOption('BBC', _t('Bbc', 'Bbc'), 3),
        SelectionOption('MINERGIE', _t('Minergie', 'Minergie'), 4),
        SelectionOption('EFFINERGIE_PLUS', _t('Effinergie Plus', 'Effinergie Plus'), 5),
        SelectionOption('HQE', _t('Hqe', 'Hqe'), 6),
        SelectionOption('THQE', _t('Thqe', 'Thqe'), 7),
        ),
        # source: data.energy.countrySpecific.fr.houseEnergyStandardType
    ),
)

# ---- estate_sub_type (11 fields) ----
DERIVED_ESTATE_SUB_TYPE_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_house',
        ttype='selection',
        label=_t('House', 'House'),
        help=_t('subtypes of a house to describe the selected estate type in detail. descriptions for the enums above: - APARTMENT_HOUSE: a building containing multiple apartments with a common entrance and sometimes services - BUNGALOW: a house that usually has only one storey, sometimes with an attic, with a flat or a low-pitched roof - CASTLE: a historical massive and imposing building usually fortified, built by the nobility, royalty or by military orders. - MANOR_HOUSE: magnificent country house, often dating from the late middle ages, in which the landed gentry used to live. - CHALET: a wooden house with…', 'subtypes of a house to describe the selected estate type in detail. descriptions for the enums above: - APARTMENT_HOUSE: a building containing multiple apartments with a common entrance and sometimes services - BUNGALOW: a house that usually has only one storey, sometimes with an attic, with a flat or a low-pitched roof - CASTLE: a historical massive and imposing building usually fortified, built by the nobility, royalty or by military orders. - MANOR_HOUSE: magnificent country house, often dating from the late middle ages, in which the landed gentry used to live. - CHALET: a wooden house with…'),
        selection=(
        SelectionOption('APARTMENT_HOUSE', _t('Apartment House', 'Apartment House'), 0),
        SelectionOption('BUNGALOW', _t('Bungalow', 'Bungalow'), 1),
        SelectionOption('CASTLE', _t('Castle', 'Castle'), 2),
        SelectionOption('MANOR_HOUSE', _t('Manor House', 'Manor House'), 3),
        SelectionOption('CHALET', _t('Chalet', 'Chalet'), 4),
        SelectionOption('FARMHOUSE', _t('Farmhouse', 'Farmhouse'), 5),
        SelectionOption('FINCA', _t('Finca', 'Finca'), 6),
        SelectionOption('GARDEN_HOUSE', _t('Garden House', 'Garden House'), 7),
        SelectionOption('GITE', _t('Gite', 'Gite'), 8),
        SelectionOption('LIVING_AND_COMMERCIAL', _t('Living And Commercial', 'Living And Commercial'), 9),
        SelectionOption('MULTI_FAMILY_HOUSE', _t('Multi Family House', 'Multi Family House'), 10),
        SelectionOption('MOUNTAIN_HUT', _t('Mountain Hut', 'Mountain Hut'), 11),
        SelectionOption('RESIDENTIAL_COMPLEX', _t('Residential Complex', 'Residential Complex'), 12),
        SelectionOption('RUSTICO', _t('Rustico', 'Rustico'), 13),
        SelectionOption('SEMIDETACHED_HOUSE', _t('Semidetached House', 'Semidetached House'), 14),
        SelectionOption('SINGLE_FAMILY_HOUSE', _t('Single Family House', 'Single Family House'), 15),
        SelectionOption('SPECIAL_REAL_ESTATE', _t('Special Real Estate', 'Special Real Estate'), 16),
        SelectionOption('TERRACE_HOUSE', _t('Terrace House', 'Terrace House'), 17),
        SelectionOption('CORNER_TERRACE_HOUSE', _t('Corner Terrace House', 'Corner Terrace House'), 18),
        SelectionOption('END_TERRACE_HOUSE', _t('End Terrace House', 'End Terrace House'), 19),
        SelectionOption('MID_TERRACE_HOUSE', _t('Mid Terrace House', 'Mid Terrace House'), 20),
        SelectionOption('TOWN_HOUSE', _t('Town House', 'Town House'), 21),
        SelectionOption('VILLA', _t('Villa', 'Villa'), 22),
        SelectionOption('MANSION', _t('Mansion', 'Mansion'), 23),
        SelectionOption('PROVENCAL_FARMHOUSE', _t('Provencal Farmhouse', 'Provencal Farmhouse'), 24),
        ),
        # source: data.estateSubType.house
    ),
    FieldSpec(
        name='x_apartment',
        ttype='selection',
        label=_t('Apartment', 'Apartment'),
        help=_t('subtypes of an apartment to describe the selected estate type in detail. descriptions for the enums above: - MULTI_STOREY: apartment that spreads over two, three or more floors connected by an inner staircase, offered as one property. a maisonette; - FLATSHARING_ROOM: single room within a flat or a house in the context of shared living - LOFT: an industrial, warehouse, or commercial space converted to an apartment - PENTHOUSE: an apartment on the highest floor of a building, that is usually equipped with high standard. Equivalent to the Swiss Attica. - STUDIO: a small flat in which the normal…', 'subtypes of an apartment to describe the selected estate type in detail. descriptions for the enums above: - MULTI_STOREY: apartment that spreads over two, three or more floors connected by an inner staircase, offered as one property. a maisonette; - FLATSHARING_ROOM: single room within a flat or a house in the context of shared living - LOFT: an industrial, warehouse, or commercial space converted to an apartment - PENTHOUSE: an apartment on the highest floor of a building, that is usually equipped with high standard. Equivalent to the Swiss Attica. - STUDIO: a small flat in which the normal…'),
        selection=(
        SelectionOption('MULTI_STOREY', _t('Multi Storey', 'Multi Storey'), 0),
        SelectionOption('FLATSHARING_ROOM', _t('Flatsharing Room', 'Flatsharing Room'), 1),
        SelectionOption('LOFT', _t('Loft', 'Loft'), 2),
        SelectionOption('PENTHOUSE', _t('Penthouse', 'Penthouse'), 3),
        SelectionOption('STUDIO', _t('Studio', 'Studio'), 4),
        SelectionOption('TERRACE', _t('Terrace', 'Terrace'), 5),
        SelectionOption('UNFINISHED_ATTIC_SPACE', _t('Unfinished Attic Space', 'Unfinished Attic Space'), 6),
        ),
        # source: data.estateSubType.apartment
    ),
    FieldSpec(
        name='x_plot',
        ttype='selection',
        label=_t('Plot', 'Plot'),
        help=_t('subtypes of a plot to describe the selected estate type in detail. Descriptions for the enums above: - LIVING: only residential buildings may be built on that plot - COMMERCIAL: only for commercial use - INDUSTRY: only for industrial use - AGRICULTURE_FORESTRY: a plot intended for farming or forestry - MIXED: a plot for mixed usage - LEISURE_FACILITY: for leisure activities such as sports, gardening, etc. - COMMERCIAL_PARC: a plot in a commercial park or a commercial park itself - SPECIAL_USE: a plot for a separate or special use - LAKESIDE_PROPERTY: a plot that adjoins a lake or the sea', 'subtypes of a plot to describe the selected estate type in detail. Descriptions for the enums above: - LIVING: only residential buildings may be built on that plot - COMMERCIAL: only for commercial use - INDUSTRY: only for industrial use - AGRICULTURE_FORESTRY: a plot intended for farming or forestry - MIXED: a plot for mixed usage - LEISURE_FACILITY: for leisure activities such as sports, gardening, etc. - COMMERCIAL_PARC: a plot in a commercial park or a commercial park itself - SPECIAL_USE: a plot for a separate or special use - LAKESIDE_PROPERTY: a plot that adjoins a lake or the sea'),
        selection=(
        SelectionOption('LIVING', _t('Living', 'Living'), 0),
        SelectionOption('COMMERCIAL', _t('Commercial', 'Commercial'), 1),
        SelectionOption('INDUSTRY', _t('Industry', 'Industry'), 2),
        SelectionOption('AGRICULTURE_FORESTRY', _t('Agriculture Forestry', 'Agriculture Forestry'), 3),
        SelectionOption('MIXED', _t('Mixed', 'Mixed'), 4),
        SelectionOption('LEISURE_FACILITY', _t('Leisure Facility', 'Leisure Facility'), 5),
        SelectionOption('COMMERCIAL_PARC', _t('Commercial Parc', 'Commercial Parc'), 6),
        SelectionOption('SPECIAL_USE', _t('Special Use', 'Special Use'), 7),
        SelectionOption('LAKESIDE_PROPERTY', _t('Lakeside Property', 'Lakeside Property'), 8),
        ),
        # source: data.estateSubType.plot
    ),
    FieldSpec(
        name='x_office',
        ttype='selection',
        label=_t('Office', 'Office'),
        help=_t('subtypes of an office property to describe the selected estate type in detail. Descriptions for the enums above: - SINGLE_OFFICE: single office room - OFFICE_SPACE: an office for several workplaces, can consist of several rooms - OFFICE_BUILDING: a building that contains different office units - OFFICE_CENTRE: a larger building that contains different office units, can also be made up of several buildings - OFFICE_STORAGE_BUILDING: combines an office building and a warehouse - MEDICAL: medical practice sometimes already equipped with medical apparatus - MEDICAL_FLOOR: more general a floor for…', 'subtypes of an office property to describe the selected estate type in detail. Descriptions for the enums above: - SINGLE_OFFICE: single office room - OFFICE_SPACE: an office for several workplaces, can consist of several rooms - OFFICE_BUILDING: a building that contains different office units - OFFICE_CENTRE: a larger building that contains different office units, can also be made up of several buildings - OFFICE_STORAGE_BUILDING: combines an office building and a warehouse - MEDICAL: medical practice sometimes already equipped with medical apparatus - MEDICAL_FLOOR: more general a floor for…'),
        selection=(
        SelectionOption('SINGLE_OFFICE', _t('Single Office', 'Single Office'), 0),
        SelectionOption('OFFICE_SPACE', _t('Office Space', 'Office Space'), 1),
        SelectionOption('OFFICE_BUILDING', _t('Office Building', 'Office Building'), 2),
        SelectionOption('OFFICE_CENTRE', _t('Office Centre', 'Office Centre'), 3),
        SelectionOption('OFFICE_STORAGE_BUILDING', _t('Office Storage Building', 'Office Storage Building'), 4),
        SelectionOption('MEDICAL', _t('Medical', 'Medical'), 5),
        SelectionOption('MEDICAL_FLOOR', _t('Medical Floor', 'Medical Floor'), 6),
        SelectionOption('MEDICAL_BUILDING', _t('Medical Building', 'Medical Building'), 7),
        SelectionOption('LIVING_AND_COMMERCIAL_BUILDING', _t('Living And Commercial Building', 'Living And Commercial Building'), 8),
        SelectionOption('ATELIER', _t('Atelier', 'Atelier'), 9),
        SelectionOption('COWORKING', _t('Coworking', 'Coworking'), 10),
        SelectionOption('OPEN_SPACE', _t('Open Space', 'Open Space'), 11),
        SelectionOption('SHARED_OFFICE', _t('Shared Office', 'Shared Office'), 12),
        ),
        # source: data.estateSubType.office
    ),
    FieldSpec(
        name='x_trading',
        ttype='selection',
        label=_t('Trading', 'Trading'),
        help=_t('subtypes of a trading related property to describe the selected estate type in detail. Descriptions for the enums above: - STORE: shop or store for retail - SHOWROOM_SPACE: a room where merchandise is exhibited for sale or where samples are displayed - SHOPPING_CENTRE: a building that contains several stores - KIOSK: a small building from which people can buy things such as sandwiches or newspapers usually through an open window or with a very small sellspace - SALES_AREA: a sellspace within another store', 'subtypes of a trading related property to describe the selected estate type in detail. Descriptions for the enums above: - STORE: shop or store for retail - SHOWROOM_SPACE: a room where merchandise is exhibited for sale or where samples are displayed - SHOPPING_CENTRE: a building that contains several stores - KIOSK: a small building from which people can buy things such as sandwiches or newspapers usually through an open window or with a very small sellspace - SALES_AREA: a sellspace within another store'),
        selection=(
        SelectionOption('STORE', _t('Store', 'Store'), 0),
        SelectionOption('SHOWROOM_SPACE', _t('Showroom Space', 'Showroom Space'), 1),
        SelectionOption('SHOPPING_CENTRE', _t('Shopping Centre', 'Shopping Centre'), 2),
        SelectionOption('KIOSK', _t('Kiosk', 'Kiosk'), 3),
        SelectionOption('SALES_AREA', _t('Sales Area', 'Sales Area'), 4),
        ),
        # source: data.estateSubType.trading
    ),
    FieldSpec(
        name='x_gastronomy_hotel',
        ttype='selection',
        label=_t('Gastronomy Hotel', 'Gastronomy Hotel'),
        help=_t('subtypes of a gastronomy and hotel related property to describe the selected estate type in detail. Descriptions for the enums above: - CAFE_BAR_PUB: a property for a cafe, a bar, a pub or something similar - RESTAURANT: a property for a restaurant - CLUB_DISCOTHEQUE: a property for club or a discotheque - HOTEL: a property for a hotel - APART_HOTEL: like a hotel, but instead of small rooms there are apartments or studios - LEISURE: a property for leisure or entertainment with gastronomy', 'subtypes of a gastronomy and hotel related property to describe the selected estate type in detail. Descriptions for the enums above: - CAFE_BAR_PUB: a property for a cafe, a bar, a pub or something similar - RESTAURANT: a property for a restaurant - CLUB_DISCOTHEQUE: a property for club or a discotheque - HOTEL: a property for a hotel - APART_HOTEL: like a hotel, but instead of small rooms there are apartments or studios - LEISURE: a property for leisure or entertainment with gastronomy'),
        selection=(
        SelectionOption('CAFE_BAR_PUB', _t('Cafe Bar Pub', 'Cafe Bar Pub'), 0),
        SelectionOption('RESTAURANT', _t('Restaurant', 'Restaurant'), 1),
        SelectionOption('CLUB_DISCOTHEQUE', _t('Club Discotheque', 'Club Discotheque'), 2),
        SelectionOption('HOTEL', _t('Hotel', 'Hotel'), 3),
        SelectionOption('APART_HOTEL', _t('Apart Hotel', 'Apart Hotel'), 4),
        SelectionOption('LEISURE', _t('Leisure', 'Leisure'), 5),
        ),
        # source: data.estateSubType.gastronomyHotel
    ),
    FieldSpec(
        name='x_storage_production',
        ttype='selection',
        label=_t('Storage Production', 'Storage Production'),
        help=_t('subtypes of a storage and production related property to describe the selected estate type in detail. Descriptions for the enums above: - WAREHOUSE_HALL: a hall for industry and storage - LOGISTICS_CENTER: - PRODUCTION_HALL: an industrial hall where something is produced - GARAGE_REPAIR: a repair shop or workshop - OUTDOOR_SPACE: an open space without a building or adjoining to a building - MISC_STORAGE: a storage property that cannot be dedicated to one of the other subTypes', 'subtypes of a storage and production related property to describe the selected estate type in detail. Descriptions for the enums above: - WAREHOUSE_HALL: a hall for industry and storage - LOGISTICS_CENTER: - PRODUCTION_HALL: an industrial hall where something is produced - GARAGE_REPAIR: a repair shop or workshop - OUTDOOR_SPACE: an open space without a building or adjoining to a building - MISC_STORAGE: a storage property that cannot be dedicated to one of the other subTypes'),
        selection=(
        SelectionOption('WAREHOUSE_HALL', _t('Warehouse Hall', 'Warehouse Hall'), 0),
        SelectionOption('LOGISTICS_CENTER', _t('Logistics Center', 'Logistics Center'), 1),
        SelectionOption('PRODUCTION_HALL', _t('Production Hall', 'Production Hall'), 2),
        SelectionOption('GARAGE_REPAIR', _t('Garage Repair', 'Garage Repair'), 3),
        SelectionOption('OUTDOOR_SPACE', _t('Outdoor Space', 'Outdoor Space'), 4),
        SelectionOption('MISC_STORAGE', _t('Misc Storage', 'Misc Storage'), 5),
        ),
        # source: data.estateSubType.storageProduction
    ),
    FieldSpec(
        name='x_agriculture_forestry',
        ttype='selection',
        label=_t('Agriculture Forestry', 'Agriculture Forestry'),
        help=_t('subtypes of a agriculture and forest related property to describe the selected estate type in detail. Descriptions for the enums above: - FARM_RANCH: land area with usually different buildings for farming and livestock - AGRICULTURE_COMPANY: farm that runs agriculture as business - GARDENING: place where plants are tended and cultivated for trading or selling - FORESTRY: management of forests, with planting, lumbering and caring for the wood - WINERY: an establishment where wine is grown and made - HUNTING: a ground for hunting - FISHING: fishery and aquaculture - RIDING: riding stables; also…', 'subtypes of a agriculture and forest related property to describe the selected estate type in detail. Descriptions for the enums above: - FARM_RANCH: land area with usually different buildings for farming and livestock - AGRICULTURE_COMPANY: farm that runs agriculture as business - GARDENING: place where plants are tended and cultivated for trading or selling - FORESTRY: management of forests, with planting, lumbering and caring for the wood - WINERY: an establishment where wine is grown and made - HUNTING: a ground for hunting - FISHING: fishery and aquaculture - RIDING: riding stables; also…'),
        selection=(
        SelectionOption('FARM_RANCH', _t('Farm Ranch', 'Farm Ranch'), 0),
        SelectionOption('AGRICULTURE_COMPANY', _t('Agriculture Company', 'Agriculture Company'), 1),
        SelectionOption('GARDENING', _t('Gardening', 'Gardening'), 2),
        SelectionOption('FORESTRY', _t('Forestry', 'Forestry'), 3),
        SelectionOption('WINERY', _t('Winery', 'Winery'), 4),
        SelectionOption('HUNTING', _t('Hunting', 'Hunting'), 5),
        SelectionOption('FISHING', _t('Fishing', 'Fishing'), 6),
        SelectionOption('RIDING', _t('Riding', 'Riding'), 7),
        SelectionOption('MISC_AGRICULTURE', _t('Misc Agriculture', 'Misc Agriculture'), 8),
        SelectionOption('ORCHARD', _t('Orchard', 'Orchard'), 9),
        ),
        # source: data.estateSubType.agricultureForestry
    ),
    FieldSpec(
        name='x_parking',
        ttype='selection',
        label=_t('Parking', 'Parking'),
        help=_t('subtypes of a parking property to describe the selected estate type in detail. Descriptions for the enums above: - OUTSIDE: a parking space that is outside not in a garage - STREET_PARKING: a parking space along the street - CARPORT: a shelter for vehicles that is open-sided and usually attached to a house - GARAGE: a building for parking one vehicle usually with a vertical rolling door - DOUBLE_GARAGE: like a garage but for two vehicles - DUPLEX: double parking on one parking space with a parking lift - GARAGE_AREA: an area with several garages only, no houses attached - PARKING_AREA: a confi…', 'subtypes of a parking property to describe the selected estate type in detail. Descriptions for the enums above: - OUTSIDE: a parking space that is outside not in a garage - STREET_PARKING: a parking space along the street - CARPORT: a shelter for vehicles that is open-sided and usually attached to a house - GARAGE: a building for parking one vehicle usually with a vertical rolling door - DOUBLE_GARAGE: like a garage but for two vehicles - DUPLEX: double parking on one parking space with a parking lift - GARAGE_AREA: an area with several garages only, no houses attached - PARKING_AREA: a confi…'),
        selection=(
        SelectionOption('OUTSIDE', _t('Outside', 'Outside'), 0),
        SelectionOption('STREET_PARKING', _t('Street Parking', 'Street Parking'), 1),
        SelectionOption('CARPORT', _t('Carport', 'Carport'), 2),
        SelectionOption('GARAGE', _t('Garage', 'Garage'), 3),
        SelectionOption('DOUBLE_GARAGE', _t('Double Garage', 'Double Garage'), 4),
        SelectionOption('DUPLEX', _t('Duplex', 'Duplex'), 5),
        SelectionOption('GARAGE_AREA', _t('Garage Area', 'Garage Area'), 6),
        SelectionOption('PARKING_AREA', _t('Parking Area', 'Parking Area'), 7),
        SelectionOption('CAR_PARK', _t('Car Park', 'Car Park'), 8),
        SelectionOption('UNDERGROUND_GARAGE', _t('Underground Garage', 'Underground Garage'), 9),
        SelectionOption('UNDERGROUND_PARKING_SPACE', _t('Underground Parking Space', 'Underground Parking Space'), 10),
        SelectionOption('BOAT_DOCK', _t('Boat Dock', 'Boat Dock'), 11),
        ),
        # source: data.estateSubType.parking
    ),
    FieldSpec(
        name='x_senior',
        ttype='selection',
        label=_t('Senior', 'Senior'),
        help=_t('subtypes for senior-oriented apartments to describe the selected estate type in detail. Descriptions for the enums above: - LIVING: apartment in a senior-oriented environment (without assistance, care and nursing) - ASSISTED_LIVING: apartment in a senior-oriented environment with assistance. Optional services and personal care are provided in a home-like, social setting, whereby the focus is on the independence of the residents. - MEDICAL_CARE: apartment in a senior-oriented clinical setting, nursing homes provide medical and personal care for people in great need of care.', 'subtypes for senior-oriented apartments to describe the selected estate type in detail. Descriptions for the enums above: - LIVING: apartment in a senior-oriented environment (without assistance, care and nursing) - ASSISTED_LIVING: apartment in a senior-oriented environment with assistance. Optional services and personal care are provided in a home-like, social setting, whereby the focus is on the independence of the residents. - MEDICAL_CARE: apartment in a senior-oriented clinical setting, nursing homes provide medical and personal care for people in great need of care.'),
        selection=(
        SelectionOption('LIVING', _t('Living', 'Living'), 0),
        SelectionOption('ASSISTED_LIVING', _t('Assisted Living', 'Assisted Living'), 1),
        SelectionOption('MEDICAL_CARE', _t('Medical Care', 'Medical Care'), 2),
        ),
        # source: data.estateSubType.senior
    ),
    FieldSpec(
        name='x_project',
        ttype='selection',
        label=_t('Project', 'Project'),
        help=_t('subtypes of a real estate project. Descriptions for the enums above: - MULTI_FAMILY_HOUSE: is a project for a multi family house, that is build as one building/project, but the individual residential units in the multi family house will be sold separately. The separated units/classifieds are assigned to the project and are also displayed accordingly on the portal. In comparison: `HOUSE.MULTI_FAMILY_HOUSE` is one property/classified, that is also sold as one! - HOUSE_PARK: a collection of different house types - SINGLE_MULTI_HOUSES: **Note:** this entry is deprecated. Use `HOUSE_PARK` instead.…', 'subtypes of a real estate project. Descriptions for the enums above: - MULTI_FAMILY_HOUSE: is a project for a multi family house, that is build as one building/project, but the individual residential units in the multi family house will be sold separately. The separated units/classifieds are assigned to the project and are also displayed accordingly on the portal. In comparison: `HOUSE.MULTI_FAMILY_HOUSE` is one property/classified, that is also sold as one! - HOUSE_PARK: a collection of different house types - SINGLE_MULTI_HOUSES: **Note:** this entry is deprecated. Use `HOUSE_PARK` instead.…'),
        selection=(
        SelectionOption('MULTI_FAMILY_HOUSE', _t('Multi Family House', 'Multi Family House'), 0),
        SelectionOption('HOUSE_PARK', _t('House Park', 'House Park'), 1),
        SelectionOption('SINGLE_MULTI_HOUSES', _t('Single Multi Houses', 'Single Multi Houses'), 2),
        SelectionOption('MISCELLANEOUS', _t('Miscellaneous', 'Miscellaneous'), 3),
        ),
        # source: data.estateSubType.project
    ),
)

# ---- estate_type (1 fields) ----
DERIVED_ESTATE_TYPE_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_estate_type',
        ttype='selection',
        label=_t('Estate Type', 'Type de bien'),
        help=_t('the general type of the property. To classify it in detail, please use the subtypes. descriptions for the enums above: - HOUSE: a building where people live in - APARTMENT: a set of rooms for living in within a building; a flat - PLOT: a piece of land - OFFICE: a room, set of rooms, or building where the business of a commercial or industrial organization or of a professional person is conducted. also medical offices are included here. - TRADING: all kind of properties concerning trading, retail and whole sale - GASTRONOMY_HOTEL: all kind of properties concerning the hotel and catering industr…', 'the general type of the property. To classify it in detail, please use the subtypes. descriptions for the enums above: - HOUSE: a building where people live in - APARTMENT: a set of rooms for living in within a building; a flat - PLOT: a piece of land - OFFICE: a room, set of rooms, or building where the business of a commercial or industrial organization or of a professional person is conducted. also medical offices are included here. - TRADING: all kind of properties concerning trading, retail and whole sale - GASTRONOMY_HOTEL: all kind of properties concerning the hotel and catering industr…'),
        selection=(
        SelectionOption('HOUSE', _t('House', 'House'), 0),
        SelectionOption('APARTMENT', _t('Apartment', 'Apartment'), 1),
        SelectionOption('PLOT', _t('Plot', 'Plot'), 2),
        SelectionOption('OFFICE', _t('Office', 'Office'), 3),
        SelectionOption('TRADING', _t('Trading', 'Trading'), 4),
        SelectionOption('GASTRONOMY_HOTEL', _t('Gastronomy Hotel', 'Gastronomy Hotel'), 5),
        SelectionOption('STORAGE_PRODUCTION', _t('Storage Production', 'Storage Production'), 6),
        SelectionOption('AGRICULTURE_FORESTRY', _t('Agriculture Forestry', 'Agriculture Forestry'), 7),
        SelectionOption('PARKING', _t('Parking', 'Parking'), 8),
        SelectionOption('SENIOR', _t('Senior', 'Senior'), 9),
        SelectionOption('PROJECT', _t('Project', 'Project'), 10),
        SelectionOption('MISCELLANEOUS', _t('Miscellaneous', 'Miscellaneous'), 11),
        ),
        # source: data.estateType
    ),
)

# ---- features (113 fields) ----
DERIVED_FEATURES_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_accessible_from_street',
        ttype='selection',
        label=_t('Accessible From Street', 'Accessible From Street'),
        help=_t('can the property be accessed directly from street.', 'can the property be accessed directly from street.'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.accessibleFromStreet
    ),
    FieldSpec(
        name='x_aircondition',
        ttype='selection',
        label=_t('Aircondition', 'Aircondition'),
        help=_t('aircondition available', 'aircondition available'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('PART', _t('Part', 'Part'), 1),
        SelectionOption('NO', _t('No', 'No'), 2),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 3),
        ),
        # source: data.features.aircondition
    ),
    FieldSpec(
        name='x_entrance_hall',
        ttype='selection',
        label=_t('Entrance Hall', 'Entrance Hall'),
        help=_t('has the property an entrance hall or has it a direct access to the rooms ?', 'has the property an entrance hall or has it a direct access to the rooms ?'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.entranceHall
    ),
    FieldSpec(
        name='x_tiles',
        ttype='selection',
        label=_t('Tiles', 'Tiles'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.tiles
    ),
    FieldSpec(
        name='x_stone',
        ttype='selection',
        label=_t('Stone', 'Stone'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.stone
    ),
    FieldSpec(
        name='x_carpet',
        ttype='selection',
        label=_t('Carpet', 'Carpet'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.carpet
    ),
    FieldSpec(
        name='x_parquet',
        ttype='selection',
        label=_t('Parquet', 'Parquet'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.parquet
    ),
    FieldSpec(
        name='x_laminate',
        ttype='selection',
        label=_t('Laminate', 'Laminate'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.laminate
    ),
    FieldSpec(
        name='x_synthetic',
        ttype='selection',
        label=_t('Synthetic', 'Synthetic'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.synthetic
    ),
    FieldSpec(
        name='x_screed',
        ttype='selection',
        label=_t('Screed', 'Screed'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.screed
    ),
    FieldSpec(
        name='x_linoleum',
        ttype='selection',
        label=_t('Linoleum', 'Linoleum'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.linoleum
    ),
    FieldSpec(
        name='x_marble',
        ttype='selection',
        label=_t('Marble', 'Marble'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.marble
    ),
    FieldSpec(
        name='x_terracotta',
        ttype='selection',
        label=_t('Terracotta', 'Terracotta'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.terracotta
    ),
    FieldSpec(
        name='x_granite',
        ttype='selection',
        label=_t('Granite', 'Granite'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.granite
    ),
    FieldSpec(
        name='x_raised_floor',
        ttype='selection',
        label=_t('Raised Floor', 'Raised Floor'),
        help=_t('provides an elevated structural floor above a solid substrate to create a hidden void for the passage of mechanical and electrical services.', 'provides an elevated structural floor above a solid substrate to create a hidden void for the passage of mechanical and electrical services.'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.raisedFloor
    ),
    FieldSpec(
        name='x_quartz',
        ttype='selection',
        label=_t('Quartz', 'Quartz'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.quartz
    ),
    FieldSpec(
        name='x_concrete',
        ttype='selection',
        label=_t('Concrete', 'Concrete'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.concrete
    ),
    FieldSpec(
        name='x_anti_dust_concrete',
        ttype='selection',
        label=_t('Anti Dust Concrete', 'Anti Dust Concrete'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.antiDustConcrete
    ),
    FieldSpec(
        name='x_wooden_plank',
        ttype='selection',
        label=_t('Wooden Plank', 'Wooden Plank'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.woodenPlank
    ),
    FieldSpec(
        name='x_anti_static',
        ttype='selection',
        label=_t('Anti Static', 'Anti Static'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.antiStatic
    ),
    FieldSpec(
        name='x_vinyl',
        ttype='selection',
        label=_t('Vinyl', 'Vinyl'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.floorCovering.vinyl
    ),
    FieldSpec(
        name='x_furnished',
        ttype='selection',
        label=_t('Furnished', 'Furnished'),
        help=_t('is the property equipped, is furniture in there?', 'is the property equipped, is furniture in there?'),
        selection=(
        SelectionOption('PART', _t('Part', 'Part'), 0),
        SelectionOption('FULL', _t('Full', 'Full'), 1),
        SelectionOption('NO', _t('No', 'No'), 2),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 3),
        ),
        # source: data.features.furnished
    ),
    FieldSpec(
        name='x_part',
        ttype='boolean',
        label=_t('Part', 'Part'),
        # source: data.features.garden.part
    ),
    FieldSpec(
        name='x_private',
        ttype='boolean',
        label=_t('Private', 'Private'),
        # source: data.features.garden.private
    ),
    FieldSpec(
        name='x_shared',
        ttype='boolean',
        label=_t('Shared', 'Shared'),
        # source: data.features.garden.shared
    ),
    FieldSpec(
        name='x_gym',
        ttype='selection',
        label=_t('Gym', 'Gym'),
        help=_t('presence of a gym in the building', 'presence of a gym in the building'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.gym
    ),
    FieldSpec(
        name='x_internet_speed_mbit',
        ttype='integer',
        label=_t('Internet Speed Mbit', 'Internet Speed Mbit'),
        help=_t('available internet speed in Mbit/s', 'available internet speed in Mbit/s'),
        # source: data.features.internet.internetSpeedMbit
    ),
    FieldSpec(
        name='x_optical_fiber',
        ttype='boolean',
        label=_t('Optical Fiber', 'Optical Fiber'),
        help=_t('Fiber to the x (FTTX; also spelled "fibre") is a generic term for any broadband network architecture using optical fiber', 'Fiber to the x (FTTX; also spelled "fibre") is a generic term for any broadband network architecture using optical fiber'),
        # source: data.features.internet.internetAvailability.opticalFiber
    ),
    FieldSpec(
        name='x_dsl',
        ttype='boolean',
        label=_t('Dsl', 'Dsl'),
        help=_t('Digital subscriber line (DSL or xDSL) is a family of technologies that are used to transmit digital data over telephone lines', 'Digital subscriber line (DSL or xDSL) is a family of technologies that are used to transmit digital data over telephone lines'),
        # source: data.features.internet.internetAvailability.dsl
    ),
    FieldSpec(
        name='x_cable',
        ttype='boolean',
        label=_t('Cable', 'Cable'),
        help=_t('Cable modem is a type of network bridge that provides bi-directional data communication', 'Cable modem is a type of network bridge that provides bi-directional data communication'),
        # source: data.features.internet.internetAvailability.cable
    ),
    FieldSpec(
        name='x_satellite',
        ttype='boolean',
        label=_t('Satellite', 'Satellite'),
        help=_t('Satellite Internet access is provided through communication satellites', 'Satellite Internet access is provided through communication satellites'),
        # source: data.features.internet.internetAvailability.satellite
    ),
    FieldSpec(
        name='x_ethernet',
        ttype='boolean',
        label=_t('Ethernet', 'Ethernet'),
        # source: data.features.internet.propertyInternetAccess.ethernet
    ),
    FieldSpec(
        name='x_wireless',
        ttype='boolean',
        label=_t('Wireless', 'Wireless'),
        # source: data.features.internet.propertyInternetAccess.wireless
    ),
    FieldSpec(
        name='x_ceiling',
        ttype='selection',
        label=_t('Ceiling', 'Ceiling'),
        help=_t('lights at the ceiling', 'lights at the ceiling'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.lighting.ceiling
    ),
    FieldSpec(
        name='x_led',
        ttype='selection',
        label=_t('Led', 'Led'),
        help=_t('LED is used as light source', 'LED is used as light source'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.lighting.led
    ),
    FieldSpec(
        name='x_lighting_window',
        ttype='selection',
        label=_t('Lighting Window', 'Lighting Window'),
        help=_t('natural light through the presence of windows', 'natural light through the presence of windows'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.lighting.window
    ),
    FieldSpec(
        name='x_mezzanine',
        ttype='selection',
        label=_t('Mezzanine', 'Mezzanine'),
        help=_t('an intermediate floor between levels of a building, used for increasing the floor area. can be used for countless applications like living, storage, work operations, etc', 'an intermediate floor between levels of a building, used for increasing the floor area. can be used for countless applications like living, storage, work operations, etc'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.mezzanine
    ),
    FieldSpec(
        name='x_property_orientation',
        ttype='selection',
        label=_t('Property Orientation', 'Property Orientation'),
        help=_t('cardinal and ordinal geographical directions', 'cardinal and ordinal geographical directions'),
        selection=(
        SelectionOption('NORTH', _t('North', 'North'), 0),
        SelectionOption('EAST', _t('East', 'East'), 1),
        SelectionOption('SOUTH', _t('South', 'South'), 2),
        SelectionOption('WEST', _t('West', 'West'), 3),
        SelectionOption('NORTH_EAST', _t('North East', 'North East'), 4),
        SelectionOption('SOUTH_EAST', _t('South East', 'South East'), 5),
        SelectionOption('NORTH_WEST', _t('North West', 'North West'), 6),
        SelectionOption('SOUTH_WEST', _t('South West', 'South West'), 7),
        SelectionOption('EAST_WEST', _t('East West', 'East West'), 8),
        SelectionOption('SOUTH_NORTH', _t('South North', 'South North'), 9),
        ),
        # source: data.features.propertyOrientation
    ),
    FieldSpec(
        name='x_receptionist',
        ttype='selection',
        label=_t('Receptionist', 'Receptionist'),
        help=_t('presence of a receptionist in the building', 'presence of a receptionist in the building'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.receptionist
    ),
    FieldSpec(
        name='x_building_intercom',
        ttype='selection',
        label=_t('Building Intercom', 'Building Intercom'),
        help=_t('allows residents to talk to visitors (and possibly see them on video) before granting them access to the building.', 'allows residents to talk to visitors (and possibly see them on video) before granting them access to the building.'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        SelectionOption('VIDEO', _t('Video', 'Video'), 3),
        ),
        # source: data.features.security.buildingIntercom
    ),
    FieldSpec(
        name='x_cam',
        ttype='selection',
        label=_t('Cam', 'Cam'),
        help=_t('camera surveillance is available', 'camera surveillance is available'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.security.cam
    ),
    FieldSpec(
        name='x_custodian',
        ttype='selection',
        label=_t('Custodian', 'Custodian'),
        help=_t('presence of a security service in the building', 'presence of a security service in the building'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.security.custodian
    ),
    FieldSpec(
        name='x_custodian_room',
        ttype='selection',
        label=_t('Custodian Room', 'Custodian Room'),
        help=_t('room for the security personnel is available in the building', 'room for the security personnel is available in the building'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.security.custodianRoom
    ),
    FieldSpec(
        name='x_digital_lock',
        ttype='selection',
        label=_t('Digital Lock', 'Digital Lock'),
        help=_t('digital or electronic locks do not require the use of physical key for access, they work by the use of e.g. RFIDs (badges, keyCards), PinCodes, fingerprints', 'digital or electronic locks do not require the use of physical key for access, they work by the use of e.g. RFIDs (badges, keyCards), PinCodes, fingerprints'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.security.digitalLock
    ),
    FieldSpec(
        name='x_emergency_call',
        ttype='selection',
        label=_t('Emergency Call', 'Emergency Call'),
        help=_t('in the event of an alarm, police or security will be called', 'in the event of an alarm, police or security will be called'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.security.emergencyCall
    ),
    FieldSpec(
        name='x_fire_sprinkler',
        ttype='selection',
        label=_t('Fire Sprinkler', 'Fire Sprinkler'),
        help=_t('presence of a fire sprinkler system', 'presence of a fire sprinkler system'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.security.fireSprinkler
    ),
    FieldSpec(
        name='x_fire_alarm',
        ttype='selection',
        label=_t('Fire Alarm', 'Fire Alarm'),
        help=_t('presence of a fire alarm system', 'presence of a fire alarm system'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.security.fireAlarm
    ),
    FieldSpec(
        name='x_intruder_alarm',
        ttype='selection',
        label=_t('Intruder Alarm', 'Intruder Alarm'),
        help=_t('presence of an intruder alarm system', 'presence of an intruder alarm system'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.security.intruderAlarm
    ),
    FieldSpec(
        name='x_reinforced_door',
        ttype='selection',
        label=_t('Reinforced Door', 'Reinforced Door'),
        help=_t('high security entrance door', 'high security entrance door'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.security.reinforcedDoor
    ),
    FieldSpec(
        name='x_safe',
        ttype='selection',
        label=_t('Safe', 'Safe'),
        help=_t('built-in safe is available in the property', 'built-in safe is available in the property'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.security.safe
    ),
    FieldSpec(
        name='x_wheelchair_use',
        ttype='selection',
        label=_t('Wheelchair Use', 'Wheelchair Use'),
        help=_t('a building is ready for wheelchair use, when it is barrierFree and the doors/passages are at least 90 cm wide', 'a building is ready for wheelchair use, when it is barrierFree and the doors/passages are at least 90 cm wide'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.wheelchairUse
    ),
    FieldSpec(
        name='x_wine_cellar',
        ttype='selection',
        label=_t('Wine Cellar', 'Wine Cellar'),
        help=_t('building has a wine cellar', 'building has a wine cellar'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.wineCellar
    ),
    FieldSpec(
        name='x_assisted_living',
        ttype='selection',
        label=_t('Assisted Living', 'Assisted Living'),
        help=_t('assisted living is offered', 'assisted living is offered'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.assistedLiving
    ),
    FieldSpec(
        name='x_chimney',
        ttype='selection',
        label=_t('Chimney', 'Chimney'),
        help=_t('presence of a chimney, indoor fireplace', 'presence of a chimney, indoor fireplace'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.chimney
    ),
    FieldSpec(
        name='x_flat_share_possible',
        ttype='selection',
        label=_t('Flat Share Possible', 'Flat Share Possible'),
        help=_t('use as shared living (app., house) is possible', 'use as shared living (app., house) is possible'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.flatSharePossible
    ),
    FieldSpec(
        name='x_hammam',
        ttype='selection',
        label=_t('Hammam', 'Hammam'),
        help=_t('hammam present, room full of steam, humid interior, generally tiled walls', 'hammam present, room full of steam, humid interior, generally tiled walls'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.hammam
    ),
    FieldSpec(
        name='x_house_cleaning_service',
        ttype='selection',
        label=_t('House Cleaning Service', 'House Cleaning Service'),
        help=_t('Is there a house cleaning service provided', 'Is there a house cleaning service provided'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.houseCleaningService
    ),
    FieldSpec(
        name='x_jacuzzi',
        ttype='selection',
        label=_t('Jacuzzi', 'Jacuzzi'),
        help=_t('presence of a jacuzzi, hot tub', 'presence of a jacuzzi, hot tub'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.jacuzzi
    ),
    FieldSpec(
        name='x_loggia',
        ttype='selection',
        label=_t('Loggia', 'Loggia'),
        help=_t('an outdoor room or gallery without windows, that is part of a house. In contrast to balcony, the loggia is surrounded by house walls on 2-3 sides.', 'an outdoor room or gallery without windows, that is part of a house. In contrast to balcony, the loggia is surrounded by house walls on 2-3 sides.'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.loggia
    ),
    FieldSpec(
        name='x_sauna',
        ttype='selection',
        label=_t('Sauna', 'Sauna'),
        help=_t('sauna present, room full of steam', 'sauna present, room full of steam'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.sauna
    ),
    FieldSpec(
        name='x_swimming_pool',
        ttype='selection',
        label=_t('Swimming Pool', 'Swimming Pool'),
        help=_t('info about a swimmingPool belonging to the property', 'info about a swimmingPool belonging to the property'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('INSIDE', _t('Inside', 'Inside'), 2),
        SelectionOption('OUTSIDE', _t('Outside', 'Outside'), 3),
        SelectionOption('INSIDE_AND_OUTSIDE', _t('Inside And Outside', 'Inside And Outside'), 4),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 5),
        ),
        # source: data.features.residential.swimmingPool
    ),
    FieldSpec(
        name='x_tennis_field',
        ttype='selection',
        label=_t('Tennis Field', 'Tennis Field'),
        help=_t('info about a tennisField belonging to the property', 'info about a tennisField belonging to the property'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        SelectionOption('PRIVATE', _t('Private', 'Private'), 3),
        SelectionOption('SHARED', _t('Shared', 'Shared'), 4),
        ),
        # source: data.features.residential.tennisField
    ),
    FieldSpec(
        name='x_tv',
        ttype='selection',
        label=_t('Tv', 'Tv'),
        help=_t('What TV connection does the property have?', 'What TV connection does the property have?'),
        selection=(
        SelectionOption('SAT', _t('Sat', 'Sat'), 0),
        SelectionOption('CABLE', _t('Cable', 'Cable'), 1),
        SelectionOption('OTHER', _t('Other', 'Other'), 2),
        ),
        # source: data.features.residential.tv
    ),
    FieldSpec(
        name='x_veranda',
        ttype='selection',
        label=_t('Veranda', 'Veranda'),
        help=_t('house has a veranda/ wintergarden', 'house has a veranda/ wintergarden'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.veranda
    ),
    FieldSpec(
        name='x_laundry_room',
        ttype='selection',
        label=_t('Laundry Room', 'Laundry Room'),
        help=_t('wash or dryroom present', 'wash or dryroom present'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.laundryRoom
    ),
    FieldSpec(
        name='x_closet',
        ttype='selection',
        label=_t('Closet', 'Closet'),
        help=_t('the property has closets for storing clothes and other personal items', 'the property has closets for storing clothes and other personal items'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.residential.closet
    ),
    FieldSpec(
        name='x_evacuation',
        ttype='selection',
        label=_t('Evacuation', 'Evacuation'),
        selection=(
        SelectionOption('ALL_SEWER', _t('All Sewer', 'All Sewer'), 0),
        SelectionOption('SEPTIC_TANK', _t('Septic Tank', 'Septic Tank'), 1),
        ),
        # source: data.features.residential.countrySpecific.fr.evacuation
    ),
    FieldSpec(
        name='x_accessible_by_trucks',
        ttype='selection',
        label=_t('Accessible By Trucks', 'Accessible By Trucks'),
        help=_t('The building has a ramp for a truck. This ramp may be separated from the access for regular cars.', 'The building has a ramp for a truck. This ramp may be separated from the access for regular cars.'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        SelectionOption('SEPARATED_TRUCK_ACCESS', _t('Separated Truck Access', 'Separated Truck Access'), 3),
        ),
        # source: data.features.commercial.accessibleByTrucks
    ),
    FieldSpec(
        name='x_auditorium',
        ttype='selection',
        label=_t('Auditorium', 'Auditorium'),
        help=_t('presence of an auditorium room', 'presence of an auditorium room'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.auditorium
    ),
    FieldSpec(
        name='x_bar',
        ttype='selection',
        label=_t('Bar', 'Bar'),
        help=_t('presence of a bar primarily for gastronomy and hotel', 'presence of a bar primarily for gastronomy and hotel'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.bar
    ),
    FieldSpec(
        name='x_building_ventilation',
        ttype='selection',
        label=_t('Building Ventilation', 'Building Ventilation'),
        help=_t('building has an aeration and ventilation system, that removes the used and "dirty" indoor air and replaces it with new, fresh, and oxygen-rich air.', 'building has an aeration and ventilation system, that removes the used and "dirty" indoor air and replaces it with new, fresh, and oxygen-rich air.'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.buildingVentilation
    ),
    FieldSpec(
        name='x_cafeteria',
        ttype='selection',
        label=_t('Cafeteria', 'Cafeteria'),
        help=_t('cafeteria available', 'cafeteria available'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.cafeteria
    ),
    FieldSpec(
        name='x_cold_store',
        ttype='selection',
        label=_t('Cold Store', 'Cold Store'),
        help=_t('property has a cold storage room', 'property has a cold storage room'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.coldStore
    ),
    FieldSpec(
        name='x_company_restaurant',
        ttype='selection',
        label=_t('Company Restaurant', 'Company Restaurant'),
        help=_t('company restaurant available', 'company restaurant available'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.companyRestaurant
    ),
    FieldSpec(
        name='x_dropped_ceiling',
        ttype='selection',
        label=_t('Dropped Ceiling', 'Dropped Ceiling'),
        help=_t('A dropped ceiling is a secondary ceiling, hung below the main (structural) ceiling. It may also be referred to as a drop ceiling, T-bar ceiling, false ceiling, suspended ceiling, grid ceiling, drop in ceiling, drop out ceiling, or ceiling tiles', 'A dropped ceiling is a secondary ceiling, hung below the main (structural) ceiling. It may also be referred to as a drop ceiling, T-bar ceiling, false ceiling, suspended ceiling, grid ceiling, drop in ceiling, drop out ceiling, or ceiling tiles'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.droppedCeiling
    ),
    FieldSpec(
        name='x_engine_generator',
        ttype='selection',
        label=_t('Engine Generator', 'Engine Generator'),
        help=_t('An engine-generator or portable generator is the combination of an electrical generator and an engine (prime mover) mounted together to form a single piece of equipment.', 'An engine-generator or portable generator is the combination of an electrical generator and an engine (prime mover) mounted together to form a single piece of equipment.'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.engineGenerator
    ),
    FieldSpec(
        name='x_exhaust_hood',
        ttype='selection',
        label=_t('Exhaust Hood', 'Exhaust Hood'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.exhaustHood
    ),
    FieldSpec(
        name='x_flexible_room_layout',
        ttype='selection',
        label=_t('Flexible Room Layout', 'Flexible Room Layout'),
        help=_t('division of the rooms can be changed, by changing the usage or by removing walls', 'division of the rooms can be changed, by changing the usage or by removing walls'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.flexibleRoomLayout
    ),
    FieldSpec(
        name='x_heated_terrace',
        ttype='selection',
        label=_t('Heated Terrace', 'Heated Terrace'),
        help=_t('terrace can be heated', 'terrace can be heated'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.heatedTerrace
    ),
    FieldSpec(
        name='x_lifting_platform',
        ttype='selection',
        label=_t('Lifting Platform', 'Lifting Platform'),
        help=_t('presence of a machinery used for lifting and loading people (e.g.wheelchairs) or goods (cars) in a vertical form.', 'presence of a machinery used for lifting and loading people (e.g.wheelchairs) or goods (cars) in a vertical form.'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.liftingPlatform
    ),
    FieldSpec(
        name='x_number_of_storage_cells',
        ttype='integer',
        label=_t('Number Of Storage Cells', 'Number Of Storage Cells'),
        help=_t('Number of storage cells in a warehouse', 'Number of storage cells in a warehouse'),
        # source: data.features.commercial.numberOfStorageCells
    ),
    FieldSpec(
        name='x_overhead_crane',
        ttype='selection',
        label=_t('Overhead Crane', 'Overhead Crane'),
        help=_t('presence of an overhead crane', 'presence of an overhead crane'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.overheadCrane
    ),
    FieldSpec(
        name='x_restaurant_seats',
        ttype='integer',
        label=_t('Restaurant Seats', 'Restaurant Seats'),
        help=_t('Number of restaurant seats inside', 'Number of restaurant seats inside'),
        # source: data.features.commercial.restaurantSeats
    ),
    FieldSpec(
        name='x_restaurant_seats_outside',
        ttype='integer',
        label=_t('Restaurant Seats Outside', 'Restaurant Seats Outside'),
        help=_t('Number of restaurant seats outside', 'Number of restaurant seats outside'),
        # source: data.features.commercial.restaurantSeatsOutside
    ),
    FieldSpec(
        name='x_tea_kitchen',
        ttype='selection',
        label=_t('Tea Kitchen', 'Tea Kitchen'),
        help=_t('building has a tea-kitchen', 'building has a tea-kitchen'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.teaKitchen
    ),
    FieldSpec(
        name='x_truck_maneuvering_area',
        ttype='selection',
        label=_t('Truck Maneuvering Area', 'Truck Maneuvering Area'),
        help=_t('presence of an area for maneuvering of trucks', 'presence of an area for maneuvering of trucks'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.truckManeuveringArea
    ),
    FieldSpec(
        name='x_vertical_sliding_door',
        ttype='selection',
        label=_t('Vertical Sliding Door', 'Vertical Sliding Door'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.commercial.verticalSlidingDoor
    ),
    FieldSpec(
        name='x_wall_siding',
        ttype='selection',
        label=_t('Wall Siding', 'Wall Siding'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        SelectionOption('DOUBLE', _t('Double', 'Double'), 3),
        SelectionOption('DECORATIVE', _t('Decorative', 'Decorative'), 4),
        ),
        # source: data.features.commercial.wallSiding
    ),
    FieldSpec(
        name='x_license_type',
        ttype='selection',
        label=_t('License Type', 'License Type'),
        selection=(
        SelectionOption('PETITE_LICENCE_RESTAURANT', _t('Petite Licence Restaurant', 'Petite Licence Restaurant'), 0),
        SelectionOption('LICENCE_RESTAURANT', _t('Licence Restaurant', 'Licence Restaurant'), 1),
        SelectionOption('LICENCE_III', _t('Licence Iii', 'Licence Iii'), 2),
        SelectionOption('LICENCE_IV', _t('Licence Iv', 'Licence Iv'), 3),
        ),
        # source: data.features.commercial.countrySpecific.fr.licenseType
    ),
    FieldSpec(
        name='x_charging_station',
        ttype='selection',
        label=_t('Charging Station', 'Charging Station'),
        help=_t('charging station for electric cars', 'charging station for electric cars'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.parking.chargingStation
    ),
    FieldSpec(
        name='x_bike_parking',
        ttype='selection',
        label=_t('Bike Parking', 'Bike Parking'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.parking.bikeParking
    ),
    FieldSpec(
        name='x_future_development_land',
        ttype='selection',
        label=_t('Future Development Land', 'Future Development Land'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.usageFor.futureDevelopmentLand
    ),
    FieldSpec(
        name='x_twinhouse',
        ttype='selection',
        label=_t('Twinhouse', 'Twinhouse'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.usageFor.twinhouse
    ),
    FieldSpec(
        name='x_single_family_house',
        ttype='selection',
        label=_t('Single Family House', 'Single Family House'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.usageFor.singleFamilyHouse
    ),
    FieldSpec(
        name='x_terrace_house',
        ttype='selection',
        label=_t('Terrace House', 'Terrace House'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.usageFor.terraceHouse
    ),
    FieldSpec(
        name='x_apartment_building',
        ttype='selection',
        label=_t('Apartment Building', 'Apartment Building'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.usageFor.apartmentBuilding
    ),
    FieldSpec(
        name='x_orchard',
        ttype='selection',
        label=_t('Orchard', 'Orchard'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.usageFor.orchard
    ),
    FieldSpec(
        name='x_farmland',
        ttype='selection',
        label=_t('Farmland', 'Farmland'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.usageFor.farmland
    ),
    FieldSpec(
        name='x_parking_space',
        ttype='selection',
        label=_t('Parking Space', 'Parking Space'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.usageFor.parkingSpace
    ),
    FieldSpec(
        name='x_usage_for_garage',
        ttype='selection',
        label=_t('Usage For Garage', 'Usage For Garage'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.usageFor.garage
    ),
    FieldSpec(
        name='x_no_development',
        ttype='selection',
        label=_t('No Development', 'No Development'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.usageFor.noDevelopment
    ),
    FieldSpec(
        name='x_development_infrastructure_district_heating',
        ttype='selection',
        label=_t('Development Infrastructure District Heating', 'Development Infrastructure District Heating'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.developmentInfrastructure.districtHeating
    ),
    FieldSpec(
        name='x_development_infrastructure_electric',
        ttype='selection',
        label=_t('Development Infrastructure Electric', 'Development Infrastructure Electric'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.developmentInfrastructure.electric
    ),
    FieldSpec(
        name='x_development_infrastructure_gas',
        ttype='selection',
        label=_t('Development Infrastructure Gas', 'Development Infrastructure Gas'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.developmentInfrastructure.gas
    ),
    FieldSpec(
        name='x_telco',
        ttype='selection',
        label=_t('Telco', 'Telco'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.developmentInfrastructure.telco
    ),
    FieldSpec(
        name='x_water',
        ttype='selection',
        label=_t('Water', 'Water'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.developmentInfrastructure.water
    ),
    FieldSpec(
        name='x_short_term_constructible',
        ttype='selection',
        label=_t('Short Term Constructible', 'Short Term Constructible'),
        help=_t('plot is shortTerm constructible', 'plot is shortTerm constructible'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.shortTermConstructible
    ),
    FieldSpec(
        name='x_brownfield',
        ttype='selection',
        label=_t('Brownfield', 'Brownfield'),
        help=_t('plot is brownfield. That is a site or industrial wasteland whose expansion, redevelopment or reuse may be complicated (presence of a hazardous substance?) Plot may be built on', 'plot is brownfield. That is a site or industrial wasteland whose expansion, redevelopment or reuse may be complicated (presence of a hazardous substance?) Plot may be built on'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.brownfield
    ),
    FieldSpec(
        name='x_building_permission',
        ttype='selection',
        label=_t('Building Permission', 'Building Permission'),
        help=_t('permission to build', 'permission to build'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.buildingPermission
    ),
    FieldSpec(
        name='x_demolition_suggested',
        ttype='selection',
        label=_t('Demolition Suggested', 'Demolition Suggested'),
        help=_t('demolition is suggested - when there is an old building on the plot', 'demolition is suggested - when there is an old building on the plot'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.demolitionSuggested
    ),
    FieldSpec(
        name='x_fenced_plot',
        ttype='selection',
        label=_t('Fenced Plot', 'Fenced Plot'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.features.plot.fencedPlot
    ),
    FieldSpec(
        name='x_is_terraced_area',
        ttype='boolean',
        label=_t('Is Terraced Area', 'Is Terraced Area'),
        help=_t('The plot is a terraced areas set, such as mediterranean Restanques or other common typical areas.', 'The plot is a terraced areas set, such as mediterranean Restanques or other common typical areas.'),
        # source: data.features.plot.isTerracedArea
    ),
    FieldSpec(
        name='x_tilt',
        ttype='selection',
        label=_t('Tilt', 'Tilt'),
        help=_t('plot tilt or inclination measured as distance covered vertically divided by horizontally => measurement in % such as: - NONE means no extra earthwork is needed for new construction - MINOR if less than 6% - SIGNIFICANT if less than 12% - STEEP if more than 12% **Note:** that terraced areas should take terraces tilt into account', 'plot tilt or inclination measured as distance covered vertically divided by horizontally => measurement in % such as: - NONE means no extra earthwork is needed for new construction - MINOR if less than 6% - SIGNIFICANT if less than 12% - STEEP if more than 12% **Note:** that terraced areas should take terraces tilt into account'),
        selection=(
        SelectionOption('NONE', _t('None', 'None'), 0),
        SelectionOption('MINOR', _t('Minor', 'Minor'), 1),
        SelectionOption('SIGNIFICANT', _t('Significant', 'Significant'), 2),
        SelectionOption('STEEP', _t('Steep', 'Steep'), 3),
        ),
        # source: data.features.plot.tilt
    ),
)

# ---- location (14 fields) ----
DERIVED_LOCATION_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_location_postalcode',
        ttype='char',
        label=_t('Location Postalcode', 'Code postal'),
        help=_t('postalcode or zip of the property location. It can be empty when not applicable. Use an empty string for unknown value.', 'postalcode or zip of the property location. It can be empty when not applicable. Use an empty string for unknown value.'),
        size=32,
        # source: data.location.postalcode
    ),
    FieldSpec(
        name='x_location_city',
        ttype='char',
        label=_t('Location City', 'Ville'),
        help=_t('city where the property is located. It can be empty when not applicable. Use an empty string for unknown value.', 'city where the property is located. It can be empty when not applicable. Use an empty string for unknown value.'),
        size=128,
        # source: data.location.city
    ),
    FieldSpec(
        name='x_location_street',
        ttype='text',
        label=_t('Location Street', 'Rue'),
        help=_t('street where the property is located. It can also be a place name or any required neighbourhood information. It can be empty when not applicable. Use an empty string for unknown value.', 'street where the property is located. It can also be a place name or any required neighbourhood information. It can be empty when not applicable. Use an empty string for unknown value.'),
        # source: data.location.street
    ),
    FieldSpec(
        name='x_location_house_number',
        ttype='char',
        label=_t('Location House Number', 'Numéro'),
        help=_t('house number where the property is located. It can be empty when not applicable. Use an empty string for unknown value.', 'house number where the property is located. It can be empty when not applicable. Use an empty string for unknown value.'),
        size=64,
        # source: data.location.houseNumber
    ),
    FieldSpec(
        name='x_unit',
        ttype='char',
        label=_t('Unit', 'Unité'),
        help=_t('An apartment, unit, office, lot, or other secondary unit designator', 'An apartment, unit, office, lot, or other secondary unit designator'),
        size=64,
        # source: data.location.unit
    ),
    FieldSpec(
        name='x_staircase',
        ttype='char',
        label=_t('Staircase', 'Escalier'),
        help=_t('numbered/lettered staircase', 'numbered/lettered staircase'),
        size=64,
        # source: data.location.staircase
    ),
    FieldSpec(
        name='x_floor_number',
        ttype='integer',
        label=_t('Floor Number', 'Étage'),
        help=_t('number of the floor in the building; 0 means ground floor, NOT first floor; 1 means first upper floor; -1 means first basement floor', 'number of the floor in the building; 0 means ground floor, NOT first floor; 1 means first upper floor; -1 means first basement floor'),
        # source: data.location.floorNumber
    ),
    FieldSpec(
        name='x_entrance',
        ttype='char',
        label=_t('Entrance', 'Entrée'),
        help=_t('numbered/lettered entrance', 'numbered/lettered entrance'),
        size=32,
        # source: data.location.entrance
    ),
    FieldSpec(
        name='x_state',
        ttype='char',
        label=_t('State', 'Région / Département'),
        help=_t('state within the country where the property is located', 'state within the country where the property is located'),
        size=128,
        # source: data.location.state
    ),
    FieldSpec(
        name='x_location_country',
        ttype='char',
        label=_t('Location Country', 'Pays'),
        help=_t('country where the property is located. **Note:** You are strongly encouraged to use ISO3166 country codes instead of country names. You can use the three-letter code (alpha-3) which is more closely related to the country name. ISO3166 country codes will be mandatory in the next major version.', 'country where the property is located. **Note:** You are strongly encouraged to use ISO3166 country codes instead of country names. You can use the three-letter code (alpha-3) which is more closely related to the country name. ISO3166 country codes will be mandatory in the next major version.'),
        size=125,
        # source: data.location.country
    ),
    FieldSpec(
        name='x_location_note_en',
        ttype='text',
        label=_t('Location Note En', 'Location Note En'),
        # source: data.location.locationNote.en
    ),
    FieldSpec(
        name='x_location_note_fr',
        ttype='text',
        label=_t('Location Note Fr', 'Location Note Fr'),
        # source: data.location.locationNote.fr
    ),
    FieldSpec(
        name='x_show_address',
        ttype='boolean',
        label=_t('Show Address', "Afficher l'adresse"),
        help=_t('This attribute has no effect. Configuration has to be set in “Localisation des biens” in MySeLogerPRO account of the customer.', 'This attribute has no effect. Configuration has to be set in “Localisation des biens” in MySeLogerPRO account of the customer.'),
        # source: data.location.showAddress
    ),
    FieldSpec(
        name='x_insee_code',
        ttype='char',
        label=_t('Insee Code', 'Insee Code'),
        help=_t('Govt Localisation Code INSEE', 'Govt Localisation Code INSEE'),
        # source: data.location.countrySpecific.fr.inseeCode
    ),
)

# ---- management (52 fields) ----
DERIVED_MANAGEMENT_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_is_immediately_available',
        ttype='boolean',
        label=_t('Is Immediately Available', 'Is Immediately Available'),
        help=_t('is ready for immediate use', 'is ready for immediate use'),
        # source: data.management.isImmediatelyAvailable
    ),
    FieldSpec(
        name='x_available_from',
        ttype='datetime',
        label=_t('Available From', 'Available From'),
        help=_t('available for use from this date and time; the date-time is an ISO 8601 formatted string', 'available for use from this date and time; the date-time is an ISO 8601 formatted string'),
        # source: data.management.availableFrom
    ),
    FieldSpec(
        name='x_available_until',
        ttype='datetime',
        label=_t('Available Until', 'Available Until'),
        help=_t('only available for use until this date and time; the date-time is an ISO 8601 formatted string', 'only available for use until this date and time; the date-time is an ISO 8601 formatted string'),
        # source: data.management.availableUntil
    ),
    FieldSpec(
        name='x_is_for_investment',
        ttype='boolean',
        label=_t('Is For Investment', 'Is For Investment'),
        help=_t('suitable as investment', 'suitable as investment'),
        # source: data.management.isForInvestment
    ),
    FieldSpec(
        name='x_heritage_protected',
        ttype='selection',
        label=_t('Heritage Protected', 'Heritage Protected'),
        help=_t('is the property under a preservation order', 'is the property under a preservation order'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.management.heritageProtected
    ),
    FieldSpec(
        name='x_market_status',
        ttype='selection',
        label=_t('Market Status', 'Market Status'),
        help=_t('marketing status of the property, is it currently sold, rented, under offer, etc. Options cannot be combined! fr: `UNDER_OFFER` si le bien est sous compromis', 'marketing status of the property, is it currently sold, rented, under offer, etc. Options cannot be combined! fr: `UNDER_OFFER` si le bien est sous compromis'),
        selection=(
        SelectionOption('SOLD', _t('Sold', 'Sold'), 0),
        SelectionOption('RENTED', _t('Rented', 'Rented'), 1),
        SelectionOption('REFERENCE', _t('Reference', 'Reference'), 2),
        SelectionOption('RESERVED', _t('Reserved', 'Reserved'), 3),
        SelectionOption('UNDER_OFFER', _t('Under Offer', 'Under Offer'), 4),
        ),
        # source: data.management.marketStatus
    ),
    FieldSpec(
        name='x_project_status',
        ttype='selection',
        label=_t('Project Status', 'Project Status'),
        help=_t('project status of the new built, new or under construction - COMMERCIAL_LAUNCH: Starting commercial offers - UNDER_CONSTRUCTION: under construction - FINISHING_WORKS: Finishing building - SHELL_WORKS: Under construction of the structure of the building shell works - PROJECT_ENDED: project ended - LAST_CHANCE: last opportunities in the project. - BUILDING_PERMISSION: Avant-première', 'project status of the new built, new or under construction - COMMERCIAL_LAUNCH: Starting commercial offers - UNDER_CONSTRUCTION: under construction - FINISHING_WORKS: Finishing building - SHELL_WORKS: Under construction of the structure of the building shell works - PROJECT_ENDED: project ended - LAST_CHANCE: last opportunities in the project. - BUILDING_PERMISSION: Avant-première'),
        selection=(
        SelectionOption('COMMERCIAL_LAUNCH', _t('Commercial Launch', 'Commercial Launch'), 0),
        SelectionOption('UNDER_CONSTRUCTION', _t('Under Construction', 'Under Construction'), 1),
        SelectionOption('FINISHING_WORKS', _t('Finishing Works', 'Finishing Works'), 2),
        SelectionOption('SHELL_WORKS', _t('Shell Works', 'Shell Works'), 3),
        SelectionOption('PROJECT_ENDED', _t('Project Ended', 'Project Ended'), 4),
        SelectionOption('LAST_CHANCE', _t('Last Chance', 'Last Chance'), 5),
        SelectionOption('BUILDING_PERMISSION', _t('Building Permission', 'Building Permission'), 6),
        ),
        # source: data.management.projectStatus
    ),
    FieldSpec(
        name='x_market_label',
        ttype='text',
        label=_t('Market Label', 'Market Label'),
        help=_t("additional to marketStatus; can be use eg on the realtor's website.", "additional to marketStatus; can be use eg on the realtor's website."),
        # source: data.management.marketLabel
    ),
    FieldSpec(
        name='x_is_rented',
        ttype='boolean',
        label=_t('Is Rented', 'Is Rented'),
        help=_t('is the purchasing property currently rented; de: ist das Kaufobjekt aktuell vermietet; fr: Indique si murs occupés ou murs libres pour un fonds de commerce', 'is the purchasing property currently rented; de: ist das Kaufobjekt aktuell vermietet; fr: Indique si murs occupés ou murs libres pour un fonds de commerce'),
        # source: data.management.isRented
    ),
    FieldSpec(
        name='x_use_for',
        ttype='selection',
        label=_t('Use For', 'Use For'),
        help=_t('Info on the usage of the property', 'Info on the usage of the property'),
        selection=(
        SelectionOption('LIVING', _t('Living', 'Living'), 0),
        SelectionOption('COMMERCIAL', _t('Commercial', 'Commercial'), 1),
        SelectionOption('MIXED', _t('Mixed', 'Mixed'), 2),
        SelectionOption('OFFICE', _t('Office', 'Office'), 3),
        SelectionOption('INDUSTRIAL', _t('Industrial', 'Industrial'), 4),
        ),
        # source: data.management.useFor
    ),
    FieldSpec(
        name='x_is_for_holiday_rental',
        ttype='boolean',
        label=_t('Is For Holiday Rental', 'Is For Holiday Rental'),
        help=_t('can be rented as holiday property to other people', 'can be rented as holiday property to other people'),
        # source: data.management.isForHolidayRental
    ),
    FieldSpec(
        name='x_favoured_gender',
        ttype='selection',
        label=_t('Favoured Gender', 'Favoured Gender'),
        help=_t('favoured gender', 'favoured gender'),
        selection=(
        SelectionOption('MALE', _t('Male', 'Male'), 0),
        SelectionOption('FEMALE', _t('Female', 'Female'), 1),
        SelectionOption('OTHER', _t('Other', 'Other'), 2),
        ),
        # source: data.management.rent.favouredGender
    ),
    FieldSpec(
        name='x_min_rental_time',
        ttype='integer',
        label=_t('Min Rental Time', 'Min Rental Time'),
        help=_t('minimum of the tenancy; see rentalTimeUnit for the unit; can also be used for lease (duration of the lease)', 'minimum of the tenancy; see rentalTimeUnit for the unit; can also be used for lease (duration of the lease)'),
        # source: data.management.rent.minRentalTime
    ),
    FieldSpec(
        name='x_max_rental_time',
        ttype='integer',
        label=_t('Max Rental Time', 'Max Rental Time'),
        help=_t('maximum of the tenancy; see rentalTimeUnit for the unit;', 'maximum of the tenancy; see rentalTimeUnit for the unit;'),
        # source: data.management.rent.maxRentalTime
    ),
    FieldSpec(
        name='x_rental_time_unit',
        ttype='selection',
        label=_t('Rental Time Unit', 'Rental Time Unit'),
        help=_t('unit of the tenancy or the lease duration', 'unit of the tenancy or the lease duration'),
        selection=(
        SelectionOption('DAY', _t('Day', 'Day'), 0),
        SelectionOption('WEEK', _t('Week', 'Week'), 1),
        SelectionOption('MONTH', _t('Month', 'Month'), 2),
        SelectionOption('YEAR', _t('Year', 'Year'), 3),
        ),
        # source: data.management.rent.rentalTimeUnit
    ),
    FieldSpec(
        name='x_certificate_of_eligibility_needed',
        ttype='selection',
        label=_t('Certificate Of Eligibility Needed', 'Certificate Of Eligibility Needed'),
        help=_t('a special certificate is needed to rent the apartment due to social or other regulation', 'a special certificate is needed to rent the apartment due to social or other regulation'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.management.rent.certificateOfEligibilityNeeded
    ),
    FieldSpec(
        name='x_max_persons',
        ttype='integer',
        label=_t('Max Persons', 'Max Persons'),
        help=_t('max. nr of persons;', 'max. nr of persons;'),
        # source: data.management.rent.maxPersons
    ),
    FieldSpec(
        name='x_non_smoker',
        ttype='selection',
        label=_t('Non Smoker', 'Non Smoker'),
        help=_t('Not allowed to smoke', 'Not allowed to smoke'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.management.rent.nonSmoker
    ),
    FieldSpec(
        name='x_pets_allowed',
        ttype='selection',
        label=_t('Pets Allowed', 'Pets Allowed'),
        help=_t('pets allowed', 'pets allowed'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.management.rent.petsAllowed
    ),
    FieldSpec(
        name='x_is_short_time_rental',
        ttype='boolean',
        label=_t('Is Short Time Rental', 'Is Short Time Rental'),
        help=_t('often associated with furnished accommodation (rooms, flats or houses) which are available for a limited period of time. its mainly used by students, young professionals, consultants and commuters who live in a city for a certain period of time (often project-, job- or study-related). short term living must not be confused with holiday flats!', 'often associated with furnished accommodation (rooms, flats or houses) which are available for a limited period of time. its mainly used by students, young professionals, consultants and commuters who live in a city for a certain period of time (often project-, job- or study-related). short term living must not be confused with holiday flats!'),
        # source: data.management.rent.isShortTimeRental
    ),
    FieldSpec(
        name='x_auction_location',
        ttype='text',
        label=_t('Auction Location', 'Auction Location'),
        help=_t('Place where the auction is held, usually the court.', 'Place where the auction is held, usually the court.'),
        # source: data.management.compulsoryAuction.auctionLocation
    ),
    FieldSpec(
        name='x_auction_space',
        ttype='char',
        label=_t('Auction Space', 'Auction Space'),
        help=_t('room number in court where the auction is held', 'room number in court where the auction is held'),
        size=64,
        # source: data.management.compulsoryAuction.auctionSpace
    ),
    FieldSpec(
        name='x_cancellation_date',
        ttype='date',
        label=_t('Cancellation Date', 'Cancellation Date'),
        help=_t('Date when a auction is stopped. The date is an ISO 8601 formatted string. de:aufhebungsTermin', 'Date when a auction is stopped. The date is an ISO 8601 formatted string. de:aufhebungsTermin'),
        # source: data.management.compulsoryAuction.cancellationDate
    ),
    FieldSpec(
        name='x_co_ownership',
        ttype='text',
        label=_t('Co Ownership', 'Co Ownership'),
        help=_t('second owner', 'second owner'),
        # source: data.management.compulsoryAuction.coOwnership
    ),
    FieldSpec(
        name='x_county_court',
        ttype='text',
        label=_t('County Court', 'County Court'),
        help=_t('court city name of the auction de: Amtsgericht', 'court city name of the auction de: Amtsgericht'),
        # source: data.management.compulsoryAuction.countyCourt
    ),
    FieldSpec(
        name='x_date_of_auction',
        ttype='datetime',
        label=_t('Date Of Auction', 'Date Of Auction'),
        help=_t('Date and time of the compulsory auction. The date is an ISO 8601 formatted string', 'Date and time of the compulsory auction. The date is an ISO 8601 formatted string'),
        # source: data.management.compulsoryAuction.dateOfAuction
    ),
    FieldSpec(
        name='x_is_discretionary_sale',
        ttype='boolean',
        label=_t('Is Discretionary Sale', 'Is Discretionary Sale'),
        help=_t('Sale opportunity before the official auction de: Freihandverkauf', 'Sale opportunity before the official auction de: Freihandverkauf'),
        # source: data.management.compulsoryAuction.isDiscretionarySale
    ),
    FieldSpec(
        name='x_distribution_plan_number',
        ttype='char',
        label=_t('Distribution Plan Number', 'Distribution Plan Number'),
        help=_t('Management number of a unit in a building de: Aufteilungsnummer', 'Management number of a unit in a building de: Aufteilungsnummer'),
        size=64,
        # source: data.management.compulsoryAuction.distributionPlanNumber
    ),
    FieldSpec(
        name='x_file_reference_at_county_court',
        ttype='text',
        label=_t('File Reference At County Court', 'File Reference At County Court'),
        help=_t('reference number of the county court de:amtsgerichtKennung', 'reference number of the county court de:amtsgerichtKennung'),
        # source: data.management.compulsoryAuction.fileReferenceAtCountyCourt
    ),
    FieldSpec(
        name='x_last_change_date',
        ttype='datetime',
        label=_t('Last Change Date', 'Last Change Date'),
        help=_t('Date when the last change was made to the information of the auction. The date is an ISO 8601 formatted string.', 'Date when the last change was made to the information of the auction. The date is an ISO 8601 formatted string.'),
        # source: data.management.compulsoryAuction.lastChangeDate
    ),
    FieldSpec(
        name='x_insolvency_administrator',
        ttype='text',
        label=_t('Insolvency Administrator', 'Insolvency Administrator'),
        help=_t('insolvency administrator de: Zwangsverwalter/Insolvenzverwalter', 'insolvency administrator de: Zwangsverwalter/Insolvenzverwalter'),
        # source: data.management.compulsoryAuction.insolvencyAdministrator
    ),
    FieldSpec(
        name='x_owner',
        ttype='text',
        label=_t('Owner', 'Owner'),
        help=_t('the owner of the property', 'the owner of the property'),
        # source: data.management.compulsoryAuction.owner
    ),
    FieldSpec(
        name='x_recordation_date',
        ttype='datetime',
        label=_t('Recordation Date', 'Recordation Date'),
        help=_t('when the property was registered as compulsory auction. The date is an ISO 8601 formatted string. de: Aufnahmedatum', 'when the property was registered as compulsory auction. The date is an ISO 8601 formatted string. de: Aufnahmedatum'),
        # source: data.management.compulsoryAuction.recordationDate
    ),
    FieldSpec(
        name='x_additional_date',
        ttype='datetime',
        label=_t('Additional Date', 'Additional Date'),
        help=_t('Additional date for the auction. The date is an ISO 8601 formatted string. de: Zusatztermin', 'Additional date for the auction. The date is an ISO 8601 formatted string. de: Zusatztermin'),
        # source: data.management.compulsoryAuction.additionalDate
    ),
    FieldSpec(
        name='x_is_without_value_limits',
        ttype='boolean',
        label=_t('Is Without Value Limits', 'Is Without Value Limits'),
        help=_t('if true, it means: free bidding at second auction date, there are no value limits anymore according to the market value. de: Wertgrenzen weggefallen', 'if true, it means: free bidding at second auction date, there are no value limits anymore according to the market value. de: Wertgrenzen weggefallen'),
        # source: data.management.compulsoryAuction.isWithoutValueLimits
    ),
    FieldSpec(
        name='x_is_splitting_auction',
        ttype='boolean',
        label=_t('Is Splitting Auction', 'Is Splitting Auction'),
        help=_t('auction mode if property is owned by more than one person de: Teilungsversteigerung', 'auction mode if property is owned by more than one person de: Teilungsversteigerung'),
        # source: data.management.compulsoryAuction.isSplittingAuction
    ),
    FieldSpec(
        name='x_is_usage_change',
        ttype='boolean',
        label=_t('Is Usage Change', 'Is Usage Change'),
        help=_t("building Usage change fr: Changement d'usage en accord avec le code de la construction et de l'habitation", "building Usage change fr: Changement d'usage en accord avec le code de la construction et de l'habitation"),
        # source: data.management.countrySpecific.fr.isUsageChange
    ),
    FieldSpec(
        name='x_is_destination_change',
        ttype='boolean',
        label=_t('Is Destination Change', 'Is Destination Change'),
        help=_t("Urban destination change. fr: Changement de destination en accord avec le code de l'urbanisme", "Urban destination change. fr: Changement de destination en accord avec le code de l'urbanisme"),
        # source: data.management.countrySpecific.fr.isDestinationChange
    ),
    FieldSpec(
        name='x_is_condo',
        ttype='boolean',
        label=_t('Is Condo', 'Is Condo'),
        help=_t('Is the property in a condominium (co-pro) ?', 'Is the property in a condominium (co-pro) ?'),
        # source: data.management.countrySpecific.fr.isCondo
    ),
    FieldSpec(
        name='x_fr_number_of_units',
        ttype='integer',
        label=_t('Fr Number Of Units', 'Fr Number Of Units'),
        help=_t('Number of lots in the condominium (nombre de lots)', 'Number of lots in the condominium (nombre de lots)'),
        # source: data.management.countrySpecific.fr.numberOfUnits
    ),
    FieldSpec(
        name='x_unit_description',
        ttype='char',
        label=_t('Unit Description', 'Unit Description'),
        help=_t('Name of the lot in the condominium', 'Name of the lot in the condominium'),
        size=64,
        # source: data.management.countrySpecific.fr.unitDescription
    ),
    FieldSpec(
        name='x_operating_costs_per_year',
        ttype='float',
        label=_t('Operating Costs Per Year', 'Operating Costs Per Year'),
        help=_t('Average annual amount of the share of the provisional budget of current expenditure', 'Average annual amount of the share of the provisional budget of current expenditure'),
        # source: data.management.countrySpecific.fr.operatingCostsPerYear
    ),
    FieldSpec(
        name='x_is_syndic_procedure',
        ttype='boolean',
        label=_t('Is Syndic Procedure', 'Is Syndic Procedure'),
        help=_t('Is the syndicate of co-owners subject to a procedure?', 'Is the syndicate of co-owners subject to a procedure?'),
        # source: data.management.countrySpecific.fr.isSyndicProcedure
    ),
    FieldSpec(
        name='x_procedure_details',
        ttype='text',
        label=_t('Procedure Details', 'Procedure Details'),
        help=_t('Details on the current procedure of the syndicate of co-owners.', 'Details on the current procedure of the syndicate of co-owners.'),
        # source: data.management.countrySpecific.fr.procedureDetails
    ),
    FieldSpec(
        name='x_commercial_lease',
        ttype='selection',
        label=_t('Commercial Lease', 'Commercial Lease'),
        help=_t('commercial lease nature: tacitely renewed every 3 years bail 3 6 9 or exempted (derogatory), short Term Lease or service Contract', 'commercial lease nature: tacitely renewed every 3 years bail 3 6 9 or exempted (derogatory), short Term Lease or service Contract'),
        selection=(
        SelectionOption('LEASE_3_6_9_YEARS', _t('Lease 3 6 9 Years', 'Lease 3 6 9 Years'), 0),
        SelectionOption('DEROGATORY', _t('Derogatory', 'Derogatory'), 1),
        SelectionOption('SHORT_TERM_LEASE', _t('Short Term Lease', 'Short Term Lease'), 2),
        SelectionOption('SERVICE_CONTRACT', _t('Service Contract', 'Service Contract'), 3),
        ),
        # source: data.management.countrySpecific.fr.commercialLease
    ),
    FieldSpec(
        name='x_commercial_lease_end_date',
        ttype='date',
        label=_t('Commercial Lease End Date', 'Commercial Lease End Date'),
        help=_t('End date of the commercial lease', 'End date of the commercial lease'),
        # source: data.management.countrySpecific.fr.commercialLeaseEndDate
    ),
    FieldSpec(
        name='x_lease_back',
        ttype='selection',
        label=_t('Lease Back', 'Lease Back'),
        help=_t('Is there any lease back for the new renter fr: Indique si il y a une cession du bail commercial pour le nouveau locataire', 'Is there any lease back for the new renter fr: Indique si il y a une cession du bail commercial pour le nouveau locataire'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.management.countrySpecific.fr.leaseBack
    ),
    FieldSpec(
        name='x_certification_e_r_p',
        ttype='selection',
        label=_t('Certification E R P', 'Certification E R P'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.management.countrySpecific.fr.certificationERP
    ),
    FieldSpec(
        name='x_certification_d_g_n_b',
        ttype='selection',
        label=_t('Certification D G N B', 'Certification D G N B'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.management.countrySpecific.fr.certificationDGNB
    ),
    FieldSpec(
        name='x_certification_b_r_e_e_a_m',
        ttype='selection',
        label=_t('Certification B R E E A M', 'Certification B R E E A M'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.management.countrySpecific.fr.certificationBREEAM
    ),
    FieldSpec(
        name='x_i_c_p_e',
        ttype='selection',
        label=_t('I C P E', 'I C P E'),
        help=_t('Toute exploitation industrielle ou agricole susceptible de créer des risques ou de provoquer des pollutions ou nuisances, notamment pour la sécurité et la santé des riverains est une installation classée.', 'Toute exploitation industrielle ou agricole susceptible de créer des risques ou de provoquer des pollutions ou nuisances, notamment pour la sécurité et la santé des riverains est une installation classée.'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.management.countrySpecific.fr.ICPE
    ),
    FieldSpec(
        name='x_unoccupied_life_annuity',
        ttype='boolean',
        label=_t('Unoccupied Life Annuity', 'Unoccupied Life Annuity'),
        help=_t('When a property is sold as life anuity, is it occupied or not.', 'When a property is sold as life anuity, is it occupied or not.'),
        # source: data.management.countrySpecific.fr.unoccupiedLifeAnnuity
    ),
)

# ---- meta_data (11 fields) ----
DERIVED_META_DATA_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_source_system',
        ttype='text',
        label=_t('Source System', 'Source System'),
        help=_t('the identifier of the sender software', 'the identifier of the sender software'),
        # source: data.metaData.source.sourceSystem
    ),
    FieldSpec(
        name='x_source_system_version',
        ttype='text',
        label=_t('Source System Version', 'Source System Version'),
        help=_t('the version of the sender software', 'the version of the sender software'),
        # source: data.metaData.source.sourceSystemVersion
    ),
    FieldSpec(
        name='x_offerer_marketing_key',
        ttype='text',
        label=_t('Offerer Marketing Key', 'Offerer Marketing Key'),
        help=_t('the human readable key of a real estate classified given by the offerer (e.g. real estate agent) within the sender software.', 'the human readable key of a real estate classified given by the offerer (e.g. real estate agent) within the sender software.'),
        # source: data.metaData.source.offererMarketingKey
    ),
    FieldSpec(
        name='x_offerer_estate_id',
        ttype='text',
        label=_t('Offerer Estate Id', 'Offerer Estate Id'),
        help=_t('unique identifier of the real estate assigned by the sender software system. Can be used for API calls', 'unique identifier of the real estate assigned by the sender software system. Can be used for API calls'),
        # source: data.metaData.source.offererEstateId
    ),
    FieldSpec(
        name='x_offerer_estate_group_id',
        ttype='text',
        label=_t('Offerer Estate Group Id', 'Offerer Estate Group Id'),
        help=_t('identifier for clustering different real estates into a defined group by the offerer (e.g. real estate agent)', 'identifier for clustering different real estates into a defined group by the offerer (e.g. real estate agent)'),
        # source: data.metaData.source.offererEstateGroupId
    ),
    FieldSpec(
        name='x_project_id',
        ttype='text',
        label=_t('Project Id', 'Project Id'),
        help=_t('identifier for grouping different real estates to a defined project', 'identifier for grouping different real estates to a defined project'),
        # source: data.metaData.projectId
    ),
    FieldSpec(
        name='x_create_date',
        ttype='datetime',
        label=_t('Create Date', 'Create Date'),
        help=_t('date when the property was initially created within the target system. will be set automatically by the receiver system. The date is an ISO 8601 formatted string', 'date when the property was initially created within the target system. will be set automatically by the receiver system. The date is an ISO 8601 formatted string'),
        # source: data.metaData.createDate
    ),
    FieldSpec(
        name='x_change_date',
        ttype='datetime',
        label=_t('Change Date', 'Change Date'),
        help=_t('date when the real estate was updated within the reciever system. will be set automatically by the reciever system. if the property was created, the change date is identical to the creation date. The date is an ISO 8601 formatted string', 'date when the real estate was updated within the reciever system. will be set automatically by the reciever system. if the property was created, the change date is identical to the creation date. The date is an ISO 8601 formatted string'),
        # source: data.metaData.changeDate
    ),
    FieldSpec(
        name='x_classified_id',
        ttype='char',
        label=_t('Classified Id', 'Classified Id'),
        help=_t('unique identifier of the classified in the portal, set by the portal. Same as in API calls and responses.', 'unique identifier of the classified in the portal, set by the portal. Same as in API calls and responses.'),
        size=36,
        # source: data.metaData.classifiedId
    ),
    FieldSpec(
        name='x_portal_web_key',
        ttype='text',
        label=_t('Portal Web Key', 'Portal Web Key'),
        help=_t('short id of the real estate classified on a public website. generated by the portal/receiver.', 'short id of the real estate classified on a public website. generated by the portal/receiver.'),
        # source: data.metaData.portalWebKey
    ),
    FieldSpec(
        name='x_nb_medias',
        ttype='float',
        label=_t('Nb Medias', 'Nb Medias'),
        help=_t('number of medias attached to the classified.', 'number of medias attached to the classified.'),
        # source: data.metaData.nbMedias
    ),
)

# ---- prices (163 fields) ----
DERIVED_PRICES_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_price_amount',
        ttype='float',
        label=_t('Price Amount', 'Price Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.buy.price.amount
    ),
    FieldSpec(
        name='x_price_vat_value',
        ttype='float',
        label=_t('Price Vat Value', 'Price Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buy.price.vatValue
    ),
    FieldSpec(
        name='x_price_vat_percent',
        ttype='float',
        label=_t('Price Vat Percent', 'Price Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buy.price.vatPercent
    ),
    FieldSpec(
        name='x_price_is_vat_included',
        ttype='boolean',
        label=_t('Price Is Vat Included', 'Price Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buy.price.isVatIncluded
    ),
    FieldSpec(
        name='x_price_price_information',
        ttype='selection',
        label=_t('Price Price Information', 'Price Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.buy.price.priceInformation
    ),
    FieldSpec(
        name='x_min_buy_amount',
        ttype='float',
        label=_t('Min Buy Amount', 'Min Buy Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.buy.minBuy.amount
    ),
    FieldSpec(
        name='x_min_buy_vat_value',
        ttype='float',
        label=_t('Min Buy Vat Value', 'Min Buy Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buy.minBuy.vatValue
    ),
    FieldSpec(
        name='x_min_buy_vat_percent',
        ttype='float',
        label=_t('Min Buy Vat Percent', 'Min Buy Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buy.minBuy.vatPercent
    ),
    FieldSpec(
        name='x_min_buy_is_vat_included',
        ttype='boolean',
        label=_t('Min Buy Is Vat Included', 'Min Buy Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buy.minBuy.isVatIncluded
    ),
    FieldSpec(
        name='x_min_buy_price_information',
        ttype='selection',
        label=_t('Min Buy Price Information', 'Min Buy Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.buy.minBuy.priceInformation
    ),
    FieldSpec(
        name='x_house_price_amount',
        ttype='float',
        label=_t('House Price Amount', 'House Price Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.buy.housePrice.amount
    ),
    FieldSpec(
        name='x_house_price_vat_value',
        ttype='float',
        label=_t('House Price Vat Value', 'House Price Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buy.housePrice.vatValue
    ),
    FieldSpec(
        name='x_house_price_vat_percent',
        ttype='float',
        label=_t('House Price Vat Percent', 'House Price Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buy.housePrice.vatPercent
    ),
    FieldSpec(
        name='x_house_price_is_vat_included',
        ttype='boolean',
        label=_t('House Price Is Vat Included', 'House Price Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buy.housePrice.isVatIncluded
    ),
    FieldSpec(
        name='x_house_price_price_information',
        ttype='selection',
        label=_t('House Price Price Information', 'House Price Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.buy.housePrice.priceInformation
    ),
    FieldSpec(
        name='x_plot_price_amount',
        ttype='float',
        label=_t('Plot Price Amount', 'Plot Price Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.buy.plotPrice.amount
    ),
    FieldSpec(
        name='x_plot_price_vat_value',
        ttype='float',
        label=_t('Plot Price Vat Value', 'Plot Price Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buy.plotPrice.vatValue
    ),
    FieldSpec(
        name='x_plot_price_vat_percent',
        ttype='float',
        label=_t('Plot Price Vat Percent', 'Plot Price Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buy.plotPrice.vatPercent
    ),
    FieldSpec(
        name='x_plot_price_is_vat_included',
        ttype='boolean',
        label=_t('Plot Price Is Vat Included', 'Plot Price Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buy.plotPrice.isVatIncluded
    ),
    FieldSpec(
        name='x_plot_price_price_information',
        ttype='selection',
        label=_t('Plot Price Price Information', 'Plot Price Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.buy.plotPrice.priceInformation
    ),
    FieldSpec(
        name='x_is_lease_buy_combi',
        ttype='boolean',
        label=_t('Is Lease Buy Combi', 'Is Lease Buy Combi'),
        help=_t('the property can also be purchased as rental purchase', 'the property can also be purchased as rental purchase'),
        # source: data.prices.buy.isLeaseBuyCombi
    ),
    FieldSpec(
        name='x_is_leasehold',
        ttype='boolean',
        label=_t('Is Leasehold', 'Is Leasehold'),
        help=_t('If the property is sold with leasehold rights. For an exact representation, please also fill in the following fields.', 'If the property is sold with leasehold rights. For an exact representation, please also fill in the following fields.'),
        # source: data.prices.buy.leasehold.isLeasehold
    ),
    FieldSpec(
        name='x_leasehold_amount',
        ttype='float',
        label=_t('Leasehold Amount', 'Leasehold Amount'),
        help=_t('amount of the leasehold rent', 'amount of the leasehold rent'),
        # source: data.prices.buy.leasehold.amount
    ),
    FieldSpec(
        name='x_leasehold_price_time_unit',
        ttype='selection',
        label=_t('Leasehold Price Time Unit', 'Leasehold Price Time Unit'),
        help=_t('when does the leaseholdRent have to be paid, per month or per year', 'when does the leaseholdRent have to be paid, per month or per year'),
        selection=(
        SelectionOption('MONTH', _t('Month', 'Month'), 0),
        SelectionOption('YEAR', _t('Year', 'Year'), 1),
        ),
        # source: data.prices.buy.leasehold.priceTimeUnit
    ),
    FieldSpec(
        name='x_duration',
        ttype='float',
        label=_t('Duration', 'Duration'),
        help=_t('the leasehold duration in years. Usually a leasehold is 50-99 years. After that time, the leasehold often can be extended.', 'the leasehold duration in years. Usually a leasehold is 50-99 years. After that time, the leasehold often can be extended.'),
        # source: data.prices.buy.leasehold.duration
    ),
    FieldSpec(
        name='x_leasehold_end_date',
        ttype='date',
        label=_t('Leasehold End Date', 'Leasehold End Date'),
        help=_t('date when the leasehold ends.', 'date when the leasehold ends.'),
        # source: data.prices.buy.leasehold.endDate
    ),
    FieldSpec(
        name='x_buy_operating_costs_amount',
        ttype='float',
        label=_t('Buy Operating Costs Amount', 'Buy Operating Costs Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.buy.operatingCosts.amount
    ),
    FieldSpec(
        name='x_buy_operating_costs_vat_value',
        ttype='float',
        label=_t('Buy Operating Costs Vat Value', 'Buy Operating Costs Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buy.operatingCosts.vatValue
    ),
    FieldSpec(
        name='x_buy_operating_costs_vat_percent',
        ttype='float',
        label=_t('Buy Operating Costs Vat Percent', 'Buy Operating Costs Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buy.operatingCosts.vatPercent
    ),
    FieldSpec(
        name='x_buy_operating_costs_is_vat_included',
        ttype='boolean',
        label=_t('Buy Operating Costs Is Vat Included', 'Buy Operating Costs Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buy.operatingCosts.isVatIncluded
    ),
    FieldSpec(
        name='x_buy_operating_costs_price_information',
        ttype='selection',
        label=_t('Buy Operating Costs Price Information', 'Buy Operating Costs Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.buy.operatingCosts.priceInformation
    ),
    FieldSpec(
        name='x_buy_operating_costs_accounting',
        ttype='selection',
        label=_t('Buy Operating Costs Accounting', 'Buy Operating Costs Accounting'),
        help=_t('How often the costs are paid and how: - FIXED: fixed amount paid each time unit - REAL_USAGE: amount calculated on real usage paid each time unit - ADJUSTMENT: fixed amount paid each time unit and regular (yearly?) adjustment based on real usage', 'How often the costs are paid and how: - FIXED: fixed amount paid each time unit - REAL_USAGE: amount calculated on real usage paid each time unit - ADJUSTMENT: fixed amount paid each time unit and regular (yearly?) adjustment based on real usage'),
        selection=(
        SelectionOption('FIXED', _t('Fixed', 'Fixed'), 0),
        SelectionOption('REAL_USAGE', _t('Real Usage', 'Real Usage'), 1),
        SelectionOption('ADJUSTMENT', _t('Adjustment', 'Adjustment'), 2),
        ),
        # source: data.prices.buy.operatingCosts.accounting
    ),
    FieldSpec(
        name='x_rental_income_amount',
        ttype='float',
        label=_t('Rental Income Amount', 'Rental Income Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.buy.rentalIncome.amount
    ),
    FieldSpec(
        name='x_rental_income_vat_value',
        ttype='float',
        label=_t('Rental Income Vat Value', 'Rental Income Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buy.rentalIncome.vatValue
    ),
    FieldSpec(
        name='x_rental_income_vat_percent',
        ttype='float',
        label=_t('Rental Income Vat Percent', 'Rental Income Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buy.rentalIncome.vatPercent
    ),
    FieldSpec(
        name='x_rental_income_is_vat_included',
        ttype='boolean',
        label=_t('Rental Income Is Vat Included', 'Rental Income Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buy.rentalIncome.isVatIncluded
    ),
    FieldSpec(
        name='x_rental_income_expect_amount',
        ttype='float',
        label=_t('Rental Income Expect Amount', 'Rental Income Expect Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.buy.rentalIncomeExpect.amount
    ),
    FieldSpec(
        name='x_rental_income_expect_vat_value',
        ttype='float',
        label=_t('Rental Income Expect Vat Value', 'Rental Income Expect Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buy.rentalIncomeExpect.vatValue
    ),
    FieldSpec(
        name='x_rental_income_expect_vat_percent',
        ttype='float',
        label=_t('Rental Income Expect Vat Percent', 'Rental Income Expect Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buy.rentalIncomeExpect.vatPercent
    ),
    FieldSpec(
        name='x_rental_income_expect_is_vat_included',
        ttype='boolean',
        label=_t('Rental Income Expect Is Vat Included', 'Rental Income Expect Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buy.rentalIncomeExpect.isVatIncluded
    ),
    FieldSpec(
        name='x_parking_price_amount',
        ttype='float',
        label=_t('Parking Price Amount', 'Parking Price Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.buy.parkingPrice.amount
    ),
    FieldSpec(
        name='x_parking_price_vat_value',
        ttype='float',
        label=_t('Parking Price Vat Value', 'Parking Price Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buy.parkingPrice.vatValue
    ),
    FieldSpec(
        name='x_parking_price_vat_percent',
        ttype='float',
        label=_t('Parking Price Vat Percent', 'Parking Price Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buy.parkingPrice.vatPercent
    ),
    FieldSpec(
        name='x_parking_price_is_vat_included',
        ttype='boolean',
        label=_t('Parking Price Is Vat Included', 'Parking Price Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buy.parkingPrice.isVatIncluded
    ),
    FieldSpec(
        name='x_parking_price_price_information',
        ttype='selection',
        label=_t('Parking Price Price Information', 'Parking Price Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.buy.parkingPrice.priceInformation
    ),
    FieldSpec(
        name='x_parking_price_parking_style',
        ttype='selection',
        label=_t('Parking Price Parking Style', 'Parking Price Parking Style'),
        help=_t('if the property has an additional garage/parking space then you can specify the parking style in details here. A parking lot can only be described by one (the most appropriate) item, not by several. Descriptions for the enums above: - OUTSIDE: a parking space that is outside, not in a garage - STREET_PARKING: a parking space along the street - CARPORT: a shelter for vehicles that is open-sided and usually attached to a house - GARAGE: a building for parking one vehicle usually with a vertical rolling door - DOUBLE_GARAGE: like a garage but for two vehicles - DUPLEX: double parking on one parki…', 'if the property has an additional garage/parking space then you can specify the parking style in details here. A parking lot can only be described by one (the most appropriate) item, not by several. Descriptions for the enums above: - OUTSIDE: a parking space that is outside, not in a garage - STREET_PARKING: a parking space along the street - CARPORT: a shelter for vehicles that is open-sided and usually attached to a house - GARAGE: a building for parking one vehicle usually with a vertical rolling door - DOUBLE_GARAGE: like a garage but for two vehicles - DUPLEX: double parking on one parki…'),
        selection=(
        SelectionOption('OUTSIDE', _t('Outside', 'Outside'), 0),
        SelectionOption('STREET_PARKING', _t('Street Parking', 'Street Parking'), 1),
        SelectionOption('CARPORT', _t('Carport', 'Carport'), 2),
        SelectionOption('GARAGE', _t('Garage', 'Garage'), 3),
        SelectionOption('DOUBLE_GARAGE', _t('Double Garage', 'Double Garage'), 4),
        SelectionOption('DUPLEX', _t('Duplex', 'Duplex'), 5),
        SelectionOption('GARAGE_AREA', _t('Garage Area', 'Garage Area'), 6),
        SelectionOption('PARKING_AREA', _t('Parking Area', 'Parking Area'), 7),
        SelectionOption('CAR_PARK', _t('Car Park', 'Car Park'), 8),
        SelectionOption('UNDERGROUND', _t('Underground', 'Underground'), 9),
        SelectionOption('BOAT_DOCK', _t('Boat Dock', 'Boat Dock'), 10),
        ),
        # source: data.prices.buy.parkingPrice.parkingStyle
    ),
    FieldSpec(
        name='x_buy_price_per_sq_unit_amount',
        ttype='float',
        label=_t('Buy Price Per Sq Unit Amount', 'Buy Price Per Sq Unit Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.buy.pricePerSqUnit.amount
    ),
    FieldSpec(
        name='x_buy_price_per_sq_unit_vat_value',
        ttype='float',
        label=_t('Buy Price Per Sq Unit Vat Value', 'Buy Price Per Sq Unit Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buy.pricePerSqUnit.vatValue
    ),
    FieldSpec(
        name='x_buy_price_per_sq_unit_vat_percent',
        ttype='float',
        label=_t('Buy Price Per Sq Unit Vat Percent', 'Buy Price Per Sq Unit Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buy.pricePerSqUnit.vatPercent
    ),
    FieldSpec(
        name='x_buy_price_per_sq_unit_is_vat_included',
        ttype='boolean',
        label=_t('Buy Price Per Sq Unit Is Vat Included', 'Buy Price Per Sq Unit Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buy.pricePerSqUnit.isVatIncluded
    ),
    FieldSpec(
        name='x_buy_price_per_sq_unit_price_information',
        ttype='selection',
        label=_t('Buy Price Per Sq Unit Price Information', 'Buy Price Per Sq Unit Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.buy.pricePerSqUnit.priceInformation
    ),
    FieldSpec(
        name='x_yield_factor',
        ttype='float',
        label=_t('Yield Factor', 'Yield Factor'),
        help=_t('for the calculation of the return. calculation: purchase price divided by annual rental income', 'for the calculation of the return. calculation: purchase price divided by annual rental income'),
        # source: data.prices.buy.yieldFactor
    ),
    FieldSpec(
        name='x_is_reduced_notary_fees',
        ttype='boolean',
        label=_t('Is Reduced Notary Fees', 'Is Reduced Notary Fees'),
        help=_t('Reduced notary fees ?', 'Reduced notary fees ?'),
        # source: data.prices.buy.countrySpecific.fr.isReducedNotaryFees
    ),
    FieldSpec(
        name='x_notary_fees_for',
        ttype='selection',
        label=_t('Notary Fees For', 'Notary Fees For'),
        selection=(
        SelectionOption('BUYER', _t('Buyer', 'Buyer'), 0),
        SelectionOption('SELLER', _t('Seller', 'Seller'), 1),
        SelectionOption('SHARED', _t('Shared', 'Shared'), 2),
        ),
        # source: data.prices.buy.countrySpecific.fr.notaryFeesFor
    ),
    FieldSpec(
        name='x_life_annuity_amount',
        ttype='float',
        label=_t('Life Annuity Amount', 'Life Annuity Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.buy.countrySpecific.fr.lifeAnnuity.amount
    ),
    FieldSpec(
        name='x_life_annuity_vat_value',
        ttype='float',
        label=_t('Life Annuity Vat Value', 'Life Annuity Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buy.countrySpecific.fr.lifeAnnuity.vatValue
    ),
    FieldSpec(
        name='x_life_annuity_vat_percent',
        ttype='float',
        label=_t('Life Annuity Vat Percent', 'Life Annuity Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buy.countrySpecific.fr.lifeAnnuity.vatPercent
    ),
    FieldSpec(
        name='x_life_annuity_is_vat_included',
        ttype='boolean',
        label=_t('Life Annuity Is Vat Included', 'Life Annuity Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buy.countrySpecific.fr.lifeAnnuity.isVatIncluded
    ),
    FieldSpec(
        name='x_life_annuity_price_information',
        ttype='selection',
        label=_t('Life Annuity Price Information', 'Life Annuity Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.buy.countrySpecific.fr.lifeAnnuity.priceInformation
    ),
    FieldSpec(
        name='x_base_rent_amount',
        ttype='float',
        label=_t('Base Rent Amount', 'Base Rent Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.baseRent.amount
    ),
    FieldSpec(
        name='x_base_rent_vat_value',
        ttype='float',
        label=_t('Base Rent Vat Value', 'Base Rent Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.baseRent.vatValue
    ),
    FieldSpec(
        name='x_base_rent_vat_percent',
        ttype='float',
        label=_t('Base Rent Vat Percent', 'Base Rent Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.baseRent.vatPercent
    ),
    FieldSpec(
        name='x_base_rent_is_vat_included',
        ttype='boolean',
        label=_t('Base Rent Is Vat Included', 'Base Rent Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.baseRent.isVatIncluded
    ),
    FieldSpec(
        name='x_base_rent_price_information',
        ttype='selection',
        label=_t('Base Rent Price Information', 'Base Rent Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.baseRent.priceInformation
    ),
    FieldSpec(
        name='x_min_rent_amount',
        ttype='float',
        label=_t('Min Rent Amount', 'Min Rent Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.minRent.amount
    ),
    FieldSpec(
        name='x_min_rent_vat_value',
        ttype='float',
        label=_t('Min Rent Vat Value', 'Min Rent Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.minRent.vatValue
    ),
    FieldSpec(
        name='x_min_rent_vat_percent',
        ttype='float',
        label=_t('Min Rent Vat Percent', 'Min Rent Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.minRent.vatPercent
    ),
    FieldSpec(
        name='x_min_rent_is_vat_included',
        ttype='boolean',
        label=_t('Min Rent Is Vat Included', 'Min Rent Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.minRent.isVatIncluded
    ),
    FieldSpec(
        name='x_min_rent_price_information',
        ttype='selection',
        label=_t('Min Rent Price Information', 'Min Rent Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.minRent.priceInformation
    ),
    FieldSpec(
        name='x_base_rent_per_year_amount',
        ttype='float',
        label=_t('Base Rent Per Year Amount', 'Base Rent Per Year Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.baseRentPerYear.amount
    ),
    FieldSpec(
        name='x_base_rent_per_year_vat_value',
        ttype='float',
        label=_t('Base Rent Per Year Vat Value', 'Base Rent Per Year Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.baseRentPerYear.vatValue
    ),
    FieldSpec(
        name='x_base_rent_per_year_vat_percent',
        ttype='float',
        label=_t('Base Rent Per Year Vat Percent', 'Base Rent Per Year Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.baseRentPerYear.vatPercent
    ),
    FieldSpec(
        name='x_base_rent_per_year_is_vat_included',
        ttype='boolean',
        label=_t('Base Rent Per Year Is Vat Included', 'Base Rent Per Year Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.baseRentPerYear.isVatIncluded
    ),
    FieldSpec(
        name='x_base_rent_per_year_price_information',
        ttype='selection',
        label=_t('Base Rent Per Year Price Information', 'Base Rent Per Year Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.baseRentPerYear.priceInformation
    ),
    FieldSpec(
        name='x_total_rent_amount',
        ttype='float',
        label=_t('Total Rent Amount', 'Total Rent Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.totalRent.amount
    ),
    FieldSpec(
        name='x_total_rent_vat_value',
        ttype='float',
        label=_t('Total Rent Vat Value', 'Total Rent Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.totalRent.vatValue
    ),
    FieldSpec(
        name='x_total_rent_vat_percent',
        ttype='float',
        label=_t('Total Rent Vat Percent', 'Total Rent Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.totalRent.vatPercent
    ),
    FieldSpec(
        name='x_total_rent_is_vat_included',
        ttype='boolean',
        label=_t('Total Rent Is Vat Included', 'Total Rent Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.totalRent.isVatIncluded
    ),
    FieldSpec(
        name='x_total_rent_price_information',
        ttype='selection',
        label=_t('Total Rent Price Information', 'Total Rent Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.totalRent.priceInformation
    ),
    FieldSpec(
        name='x_lease_amount',
        ttype='float',
        label=_t('Lease Amount', 'Lease Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.lease.amount
    ),
    FieldSpec(
        name='x_lease_vat_value',
        ttype='float',
        label=_t('Lease Vat Value', 'Lease Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.lease.vatValue
    ),
    FieldSpec(
        name='x_lease_vat_percent',
        ttype='float',
        label=_t('Lease Vat Percent', 'Lease Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.lease.vatPercent
    ),
    FieldSpec(
        name='x_lease_is_vat_included',
        ttype='boolean',
        label=_t('Lease Is Vat Included', 'Lease Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.lease.isVatIncluded
    ),
    FieldSpec(
        name='x_lease_price_information',
        ttype='selection',
        label=_t('Lease Price Information', 'Lease Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.lease.priceInformation
    ),
    FieldSpec(
        name='x_rent_operating_costs_amount',
        ttype='float',
        label=_t('Rent Operating Costs Amount', 'Rent Operating Costs Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.operatingCosts.amount
    ),
    FieldSpec(
        name='x_rent_operating_costs_vat_value',
        ttype='float',
        label=_t('Rent Operating Costs Vat Value', 'Rent Operating Costs Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.operatingCosts.vatValue
    ),
    FieldSpec(
        name='x_rent_operating_costs_vat_percent',
        ttype='float',
        label=_t('Rent Operating Costs Vat Percent', 'Rent Operating Costs Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.operatingCosts.vatPercent
    ),
    FieldSpec(
        name='x_rent_operating_costs_is_vat_included',
        ttype='boolean',
        label=_t('Rent Operating Costs Is Vat Included', 'Rent Operating Costs Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.operatingCosts.isVatIncluded
    ),
    FieldSpec(
        name='x_rent_operating_costs_price_information',
        ttype='selection',
        label=_t('Rent Operating Costs Price Information', 'Rent Operating Costs Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.operatingCosts.priceInformation
    ),
    FieldSpec(
        name='x_rent_operating_costs_accounting',
        ttype='selection',
        label=_t('Rent Operating Costs Accounting', 'Rent Operating Costs Accounting'),
        help=_t('How often the costs are paid and how: - FIXED: fixed amount paid each time unit - REAL_USAGE: amount calculated on real usage paid each time unit - ADJUSTMENT: fixed amount paid each time unit and regular (yearly?) adjustment based on real usage', 'How often the costs are paid and how: - FIXED: fixed amount paid each time unit - REAL_USAGE: amount calculated on real usage paid each time unit - ADJUSTMENT: fixed amount paid each time unit and regular (yearly?) adjustment based on real usage'),
        selection=(
        SelectionOption('FIXED', _t('Fixed', 'Fixed'), 0),
        SelectionOption('REAL_USAGE', _t('Real Usage', 'Real Usage'), 1),
        SelectionOption('ADJUSTMENT', _t('Adjustment', 'Adjustment'), 2),
        ),
        # source: data.prices.rent.operatingCosts.accounting
    ),
    FieldSpec(
        name='x_heating_costs_amount',
        ttype='float',
        label=_t('Heating Costs Amount', 'Heating Costs Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.heatingCosts.amount
    ),
    FieldSpec(
        name='x_heating_costs_vat_value',
        ttype='float',
        label=_t('Heating Costs Vat Value', 'Heating Costs Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.heatingCosts.vatValue
    ),
    FieldSpec(
        name='x_heating_costs_vat_percent',
        ttype='float',
        label=_t('Heating Costs Vat Percent', 'Heating Costs Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.heatingCosts.vatPercent
    ),
    FieldSpec(
        name='x_heating_costs_is_vat_included',
        ttype='boolean',
        label=_t('Heating Costs Is Vat Included', 'Heating Costs Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.heatingCosts.isVatIncluded
    ),
    FieldSpec(
        name='x_heating_costs_price_information',
        ttype='selection',
        label=_t('Heating Costs Price Information', 'Heating Costs Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.heatingCosts.priceInformation
    ),
    FieldSpec(
        name='x_heating_costs_accounting',
        ttype='selection',
        label=_t('Heating Costs Accounting', 'Heating Costs Accounting'),
        help=_t('How often the costs are paid and how: - FIXED: fixed amount paid each time unit - REAL_USAGE: amount calculated on real usage paid each time unit - ADJUSTMENT: fixed amount paid each time unit and regular (yearly?) adjustment based on real usage', 'How often the costs are paid and how: - FIXED: fixed amount paid each time unit - REAL_USAGE: amount calculated on real usage paid each time unit - ADJUSTMENT: fixed amount paid each time unit and regular (yearly?) adjustment based on real usage'),
        selection=(
        SelectionOption('FIXED', _t('Fixed', 'Fixed'), 0),
        SelectionOption('REAL_USAGE', _t('Real Usage', 'Real Usage'), 1),
        SelectionOption('ADJUSTMENT', _t('Adjustment', 'Adjustment'), 2),
        ),
        # source: data.prices.rent.heatingCosts.accounting
    ),
    FieldSpec(
        name='x_is_heating_included_in_o_c',
        ttype='boolean',
        label=_t('Is Heating Included In O C', 'Is Heating Included In O C'),
        help=_t('are the costs for heating already included in the operating costs?', 'are the costs for heating already included in the operating costs?'),
        # source: data.prices.rent.isHeatingIncludedInOC
    ),
    FieldSpec(
        name='x_is_heating_included_in_t_r',
        ttype='boolean',
        label=_t('Is Heating Included In T R', 'Is Heating Included In T R'),
        help=_t('are the costs for heating already included in the total rent?', 'are the costs for heating already included in the total rent?'),
        # source: data.prices.rent.isHeatingIncludedInTR
    ),
    FieldSpec(
        name='x_rent_price_per_sq_unit_amount',
        ttype='float',
        label=_t('Rent Price Per Sq Unit Amount', 'Rent Price Per Sq Unit Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.pricePerSqUnit.amount
    ),
    FieldSpec(
        name='x_rent_price_per_sq_unit_vat_value',
        ttype='float',
        label=_t('Rent Price Per Sq Unit Vat Value', 'Rent Price Per Sq Unit Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.pricePerSqUnit.vatValue
    ),
    FieldSpec(
        name='x_rent_price_per_sq_unit_vat_percent',
        ttype='float',
        label=_t('Rent Price Per Sq Unit Vat Percent', 'Rent Price Per Sq Unit Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.pricePerSqUnit.vatPercent
    ),
    FieldSpec(
        name='x_rent_price_per_sq_unit_is_vat_included',
        ttype='boolean',
        label=_t('Rent Price Per Sq Unit Is Vat Included', 'Rent Price Per Sq Unit Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.pricePerSqUnit.isVatIncluded
    ),
    FieldSpec(
        name='x_rent_price_per_sq_unit_price_information',
        ttype='selection',
        label=_t('Rent Price Per Sq Unit Price Information', 'Rent Price Per Sq Unit Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.pricePerSqUnit.priceInformation
    ),
    FieldSpec(
        name='x_price_per_sq_unit_per_year_amount',
        ttype='float',
        label=_t('Price Per Sq Unit Per Year Amount', 'Price Per Sq Unit Per Year Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.pricePerSqUnitPerYear.amount
    ),
    FieldSpec(
        name='x_price_per_sq_unit_per_year_vat_value',
        ttype='float',
        label=_t('Price Per Sq Unit Per Year Vat Value', 'Price Per Sq Unit Per Year Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.pricePerSqUnitPerYear.vatValue
    ),
    FieldSpec(
        name='x_price_per_sq_unit_per_year_vat_percent',
        ttype='float',
        label=_t('Price Per Sq Unit Per Year Vat Percent', 'Price Per Sq Unit Per Year Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.pricePerSqUnitPerYear.vatPercent
    ),
    FieldSpec(
        name='x_price_per_sq_unit_per_year_is_vat_included',
        ttype='boolean',
        label=_t('Price Per Sq Unit Per Year Is Vat Included', 'Price Per Sq Unit Per Year Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.pricePerSqUnitPerYear.isVatIncluded
    ),
    FieldSpec(
        name='x_price_per_sq_unit_per_year_price_information',
        ttype='selection',
        label=_t('Price Per Sq Unit Per Year Price Information', 'Price Per Sq Unit Per Year Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.pricePerSqUnitPerYear.priceInformation
    ),
    FieldSpec(
        name='x_rent_price_time_unit',
        ttype='selection',
        label=_t('Rent Price Time Unit', 'Rent Price Time Unit'),
        help=_t('time unit for the rent prices. Unless specified differently, Default is MONTH!', 'time unit for the rent prices. Unless specified differently, Default is MONTH!'),
        selection=(
        SelectionOption('DAY', _t('Day', 'Day'), 0),
        SelectionOption('WEEK', _t('Week', 'Week'), 1),
        SelectionOption('MONTH', _t('Month', 'Month'), 2),
        SelectionOption('YEAR', _t('Year', 'Year'), 3),
        ),
        # source: data.prices.rent.priceTimeUnit
    ),
    FieldSpec(
        name='x_is_parking_price_included',
        ttype='boolean',
        label=_t('Is Parking Price Included', 'Is Parking Price Included'),
        help=_t('is the parking space (if available) included in the rent', 'is the parking space (if available) included in the rent'),
        # source: data.prices.rent.isParkingPriceIncluded
    ),
    FieldSpec(
        name='x_parking_rent_amount',
        ttype='float',
        label=_t('Parking Rent Amount', 'Parking Rent Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.parkingRent.amount
    ),
    FieldSpec(
        name='x_parking_rent_vat_value',
        ttype='float',
        label=_t('Parking Rent Vat Value', 'Parking Rent Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.parkingRent.vatValue
    ),
    FieldSpec(
        name='x_parking_rent_vat_percent',
        ttype='float',
        label=_t('Parking Rent Vat Percent', 'Parking Rent Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.parkingRent.vatPercent
    ),
    FieldSpec(
        name='x_parking_rent_is_vat_included',
        ttype='boolean',
        label=_t('Parking Rent Is Vat Included', 'Parking Rent Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.parkingRent.isVatIncluded
    ),
    FieldSpec(
        name='x_parking_rent_price_information',
        ttype='selection',
        label=_t('Parking Rent Price Information', 'Parking Rent Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.parkingRent.priceInformation
    ),
    FieldSpec(
        name='x_parking_rent_parking_style',
        ttype='selection',
        label=_t('Parking Rent Parking Style', 'Parking Rent Parking Style'),
        help=_t('if the property has an additional garage/parking space then you can specify the parking style in details here. A parking lot can only be described by one (the most appropriate) item, not by several. Descriptions for the enums above: - OUTSIDE: a parking space that is outside, not in a garage - STREET_PARKING: a parking space along the street - CARPORT: a shelter for vehicles that is open-sided and usually attached to a house - GARAGE: a building for parking one vehicle usually with a vertical rolling door - DOUBLE_GARAGE: like a garage but for two vehicles - DUPLEX: double parking on one parki…', 'if the property has an additional garage/parking space then you can specify the parking style in details here. A parking lot can only be described by one (the most appropriate) item, not by several. Descriptions for the enums above: - OUTSIDE: a parking space that is outside, not in a garage - STREET_PARKING: a parking space along the street - CARPORT: a shelter for vehicles that is open-sided and usually attached to a house - GARAGE: a building for parking one vehicle usually with a vertical rolling door - DOUBLE_GARAGE: like a garage but for two vehicles - DUPLEX: double parking on one parki…'),
        selection=(
        SelectionOption('OUTSIDE', _t('Outside', 'Outside'), 0),
        SelectionOption('STREET_PARKING', _t('Street Parking', 'Street Parking'), 1),
        SelectionOption('CARPORT', _t('Carport', 'Carport'), 2),
        SelectionOption('GARAGE', _t('Garage', 'Garage'), 3),
        SelectionOption('DOUBLE_GARAGE', _t('Double Garage', 'Double Garage'), 4),
        SelectionOption('DUPLEX', _t('Duplex', 'Duplex'), 5),
        SelectionOption('GARAGE_AREA', _t('Garage Area', 'Garage Area'), 6),
        SelectionOption('PARKING_AREA', _t('Parking Area', 'Parking Area'), 7),
        SelectionOption('CAR_PARK', _t('Car Park', 'Car Park'), 8),
        SelectionOption('UNDERGROUND', _t('Underground', 'Underground'), 9),
        SelectionOption('BOAT_DOCK', _t('Boat Dock', 'Boat Dock'), 10),
        ),
        # source: data.prices.rent.parkingRent.parkingStyle
    ),
    FieldSpec(
        name='x_deposit_note_en',
        ttype='text',
        label=_t('Deposit Note En', 'Deposit Note En'),
        # source: data.prices.rent.depositNote.en
    ),
    FieldSpec(
        name='x_deposit_note_fr',
        ttype='text',
        label=_t('Deposit Note Fr', 'Deposit Note Fr'),
        # source: data.prices.rent.depositNote.fr
    ),
    FieldSpec(
        name='x_lease_right_amount',
        ttype='float',
        label=_t('Lease Right Amount', 'Lease Right Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.countrySpecific.fr.leaseRight.amount
    ),
    FieldSpec(
        name='x_lease_right_vat_value',
        ttype='float',
        label=_t('Lease Right Vat Value', 'Lease Right Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.countrySpecific.fr.leaseRight.vatValue
    ),
    FieldSpec(
        name='x_lease_right_vat_percent',
        ttype='float',
        label=_t('Lease Right Vat Percent', 'Lease Right Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.countrySpecific.fr.leaseRight.vatPercent
    ),
    FieldSpec(
        name='x_lease_right_is_vat_included',
        ttype='boolean',
        label=_t('Lease Right Is Vat Included', 'Lease Right Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.countrySpecific.fr.leaseRight.isVatIncluded
    ),
    FieldSpec(
        name='x_lease_right_price_information',
        ttype='selection',
        label=_t('Lease Right Price Information', 'Lease Right Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.countrySpecific.fr.leaseRight.priceInformation
    ),
    FieldSpec(
        name='x_access_price_amount',
        ttype='float',
        label=_t('Access Price Amount', 'Access Price Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.rent.countrySpecific.fr.accessPrice.amount
    ),
    FieldSpec(
        name='x_access_price_vat_value',
        ttype='float',
        label=_t('Access Price Vat Value', 'Access Price Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.rent.countrySpecific.fr.accessPrice.vatValue
    ),
    FieldSpec(
        name='x_access_price_vat_percent',
        ttype='float',
        label=_t('Access Price Vat Percent', 'Access Price Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.rent.countrySpecific.fr.accessPrice.vatPercent
    ),
    FieldSpec(
        name='x_access_price_is_vat_included',
        ttype='boolean',
        label=_t('Access Price Is Vat Included', 'Access Price Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.rent.countrySpecific.fr.accessPrice.isVatIncluded
    ),
    FieldSpec(
        name='x_access_price_price_information',
        ttype='selection',
        label=_t('Access Price Price Information', 'Access Price Price Information'),
        help=_t('- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.', '- PRICE_ON_DEMAND: specific flag for displaying this price on the portal/website. If PRICE_ON_DEMAND is chosen, the price MUST NOT be shown! It may only be used as search price! - BASIS_FOR_NEGOTIATION: the price is not fixed, it is negotiable. If the price is FIXED, priceInformation should not be sent.'),
        selection=(
        SelectionOption('PRICE_ON_DEMAND', _t('Price On Demand', 'Price On Demand'), 0),
        SelectionOption('BASIS_FOR_NEGOTIATION', _t('Basis For Negotiation', 'Basis For Negotiation'), 1),
        ),
        # source: data.prices.rent.countrySpecific.fr.accessPrice.priceInformation
    ),
    FieldSpec(
        name='x_max_regulated_rent',
        ttype='float',
        label=_t('Max Regulated Rent', 'Max Regulated Rent'),
        help=_t('The maximum regulated rent price. This amount is mandatory when the property is located into a regulated rent zone.', 'The maximum regulated rent price. This amount is mandatory when the property is located into a regulated rent zone.'),
        # source: data.prices.rent.countrySpecific.fr.maxRegulatedRent
    ),
    FieldSpec(
        name='x_over_regulated_rent',
        ttype='float',
        label=_t('Over Regulated Rent', 'Over Regulated Rent'),
        help=_t('When the rent price exceeds the (max) regulated rent price. The amount above is mandatory.', 'When the rent price exceeds the (max) regulated rent price. The amount above is mandatory.'),
        # source: data.prices.rent.countrySpecific.fr.overRegulatedRent
    ),
    FieldSpec(
        name='x_auction_proceeds_amount',
        ttype='float',
        label=_t('Auction Proceeds Amount', 'Auction Proceeds Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.compulsoryAuction.auctionProceeds.amount
    ),
    FieldSpec(
        name='x_auction_proceeds_vat_value',
        ttype='float',
        label=_t('Auction Proceeds Vat Value', 'Auction Proceeds Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.compulsoryAuction.auctionProceeds.vatValue
    ),
    FieldSpec(
        name='x_auction_proceeds_vat_percent',
        ttype='float',
        label=_t('Auction Proceeds Vat Percent', 'Auction Proceeds Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.compulsoryAuction.auctionProceeds.vatPercent
    ),
    FieldSpec(
        name='x_auction_proceeds_is_vat_included',
        ttype='boolean',
        label=_t('Auction Proceeds Is Vat Included', 'Auction Proceeds Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.compulsoryAuction.auctionProceeds.isVatIncluded
    ),
    FieldSpec(
        name='x_bidding_guarantee_amount',
        ttype='float',
        label=_t('Bidding Guarantee Amount', 'Bidding Guarantee Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.compulsoryAuction.biddingGuarantee.amount
    ),
    FieldSpec(
        name='x_bidding_guarantee_vat_value',
        ttype='float',
        label=_t('Bidding Guarantee Vat Value', 'Bidding Guarantee Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.compulsoryAuction.biddingGuarantee.vatValue
    ),
    FieldSpec(
        name='x_bidding_guarantee_vat_percent',
        ttype='float',
        label=_t('Bidding Guarantee Vat Percent', 'Bidding Guarantee Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.compulsoryAuction.biddingGuarantee.vatPercent
    ),
    FieldSpec(
        name='x_bidding_guarantee_is_vat_included',
        ttype='boolean',
        label=_t('Bidding Guarantee Is Vat Included', 'Bidding Guarantee Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.compulsoryAuction.biddingGuarantee.isVatIncluded
    ),
    FieldSpec(
        name='x_market_value_amount',
        ttype='float',
        label=_t('Market Value Amount', 'Market Value Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.compulsoryAuction.marketValue.amount
    ),
    FieldSpec(
        name='x_market_value_vat_value',
        ttype='float',
        label=_t('Market Value Vat Value', 'Market Value Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.compulsoryAuction.marketValue.vatValue
    ),
    FieldSpec(
        name='x_market_value_vat_percent',
        ttype='float',
        label=_t('Market Value Vat Percent', 'Market Value Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.compulsoryAuction.marketValue.vatPercent
    ),
    FieldSpec(
        name='x_market_value_is_vat_included',
        ttype='boolean',
        label=_t('Market Value Is Vat Included', 'Market Value Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.compulsoryAuction.marketValue.isVatIncluded
    ),
    FieldSpec(
        name='x_minimum_bid_amount',
        ttype='float',
        label=_t('Minimum Bid Amount', 'Minimum Bid Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.compulsoryAuction.minimumBid.amount
    ),
    FieldSpec(
        name='x_minimum_bid_vat_value',
        ttype='float',
        label=_t('Minimum Bid Vat Value', 'Minimum Bid Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.compulsoryAuction.minimumBid.vatValue
    ),
    FieldSpec(
        name='x_minimum_bid_vat_percent',
        ttype='float',
        label=_t('Minimum Bid Vat Percent', 'Minimum Bid Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.compulsoryAuction.minimumBid.vatPercent
    ),
    FieldSpec(
        name='x_minimum_bid_is_vat_included',
        ttype='boolean',
        label=_t('Minimum Bid Is Vat Included', 'Minimum Bid Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.compulsoryAuction.minimumBid.isVatIncluded
    ),
    FieldSpec(
        name='x_min_price_amount',
        ttype='float',
        label=_t('Min Price Amount', 'Min Price Amount'),
        help=_t('this is the lower price limit. the buy price may be higher, but it must by no means be lower.', 'this is the lower price limit. the buy price may be higher, but it must by no means be lower.'),
        # source: data.prices.buyAuction.minPrice.amount
    ),
    FieldSpec(
        name='x_min_price_vat_value',
        ttype='float',
        label=_t('Min Price Vat Value', 'Min Price Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.buyAuction.minPrice.vatValue
    ),
    FieldSpec(
        name='x_min_price_vat_percent',
        ttype='float',
        label=_t('Min Price Vat Percent', 'Min Price Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.buyAuction.minPrice.vatPercent
    ),
    FieldSpec(
        name='x_min_price_is_vat_included',
        ttype='boolean',
        label=_t('Min Price Is Vat Included', 'Min Price Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.buyAuction.minPrice.isVatIncluded
    ),
    FieldSpec(
        name='x_start_offer_phase',
        ttype='date',
        label=_t('Start Offer Phase', 'Start Offer Phase'),
        help=_t('start date when offers can be made. must be an ISO 8601 formatted string', 'start date when offers can be made. must be an ISO 8601 formatted string'),
        # source: data.prices.buyAuction.startOfferPhase
    ),
    FieldSpec(
        name='x_end_offer_phase',
        ttype='date',
        label=_t('End Offer Phase', 'End Offer Phase'),
        help=_t('end date until offers are accepted; must be an ISO 8601 formatted string', 'end date until offers are accepted; must be an ISO 8601 formatted string'),
        # source: data.prices.buyAuction.endOfferPhase
    ),
    FieldSpec(
        name='x_brokerage_fee_amount',
        ttype='float',
        label=_t('Brokerage Fee Amount', 'Brokerage Fee Amount'),
        help=_t('amount of the select priceType', 'amount of the select priceType'),
        # source: data.prices.brokerageFee.amount
    ),
    FieldSpec(
        name='x_brokerage_fee_vat_value',
        ttype='float',
        label=_t('Brokerage Fee Vat Value', 'Brokerage Fee Vat Value'),
        help=_t('the vat value in currency', 'the vat value in currency'),
        # source: data.prices.brokerageFee.vatValue
    ),
    FieldSpec(
        name='x_brokerage_fee_vat_percent',
        ttype='float',
        label=_t('Brokerage Fee Vat Percent', 'Brokerage Fee Vat Percent'),
        help=_t('the vat value in percent', 'the vat value in percent'),
        # source: data.prices.brokerageFee.vatPercent
    ),
    FieldSpec(
        name='x_brokerage_fee_is_vat_included',
        ttype='boolean',
        label=_t('Brokerage Fee Is Vat Included', 'Brokerage Fee Is Vat Included'),
        help=_t('vat is included in the price', 'vat is included in the price'),
        # source: data.prices.brokerageFee.isVatIncluded
    ),
    FieldSpec(
        name='x_show_price',
        ttype='boolean',
        label=_t('Show Price', 'Show Price'),
        help=_t('general setting for displaying the price on the portal/ website', 'general setting for displaying the price on the portal/ website'),
        # source: data.prices.showPrice
    ),
    FieldSpec(
        name='x_price_note_en',
        ttype='text',
        label=_t('Price Note En', 'Price Note En'),
        # source: data.prices.priceNote.en
    ),
    FieldSpec(
        name='x_price_note_fr',
        ttype='text',
        label=_t('Price Note Fr', 'Price Note Fr'),
        # source: data.prices.priceNote.fr
    ),
    FieldSpec(
        name='x_tax_regime',
        ttype='char',
        label=_t('Tax Regime', 'Tax Regime'),
        # source: data.prices.countrySpecific.fr.taxRegime
    ),
    FieldSpec(
        name='x_residential_lease_type',
        ttype='char',
        label=_t('Residential Lease Type', 'Residential Lease Type'),
        help=_t('Residential lease type. fr:Nature du bail résidentiel Loi 89, meblé ou Loi 48...', 'Residential lease type. fr:Nature du bail résidentiel Loi 89, meblé ou Loi 48...'),
        # source: data.prices.countrySpecific.fr.residentialLeaseType
    ),
    FieldSpec(
        name='x_is_p_t_zeligible',
        ttype='boolean',
        label=_t('Is P T Zeligible', 'Is P T Zeligible'),
        help=_t('is the property eligible for the zero rate loan? fr: est-ce que le bien est éligible au prêt à taux zéro ?', 'is the property eligible for the zero rate loan? fr: est-ce que le bien est éligible au prêt à taux zéro ?'),
        # source: data.prices.countrySpecific.fr.isPTZeligible
    ),
    FieldSpec(
        name='x_tax_reduction_zone',
        ttype='selection',
        label=_t('Tax Reduction Zone', 'Tax Reduction Zone'),
        help=_t('In France and Belgium, the buyers or landlords can get tax reductions when they buy or rent a new built property. The tax reduction level depends on the geographic zone to which the property belongs.', 'In France and Belgium, the buyers or landlords can get tax reductions when they buy or rent a new built property. The tax reduction level depends on the geographic zone to which the property belongs.'),
        selection=(
        SelectionOption('A', _t('A', 'A'), 0),
        SelectionOption('A_BIS', _t('A Bis', 'A Bis'), 1),
        SelectionOption('B1', _t('B1', 'B1'), 2),
        SelectionOption('B2', _t('B2', 'B2'), 3),
        SelectionOption('C', _t('C', 'C'), 4),
        ),
        # source: data.prices.countrySpecific.fr.taxReductionZone
    ),
)

# ---- spaces (30 fields) ----
DERIVED_SPACES_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_space_measure_unit',
        ttype='selection',
        label=_t('Space Measure Unit', 'Space Measure Unit'),
        help=_t('measure unit for the space (square meter by default).', 'measure unit for the space (square meter by default).'),
        selection=(
        SelectionOption('SQUARE_METER', _t('Square Meter', 'Square Meter'), 0),
        SelectionOption('SQUARE_INCH', _t('Square Inch', 'Square Inch'), 1),
        SelectionOption('SQUARE_FOOT', _t('Square Foot', 'Square Foot'), 2),
        SelectionOption('SQUARE_YARD', _t('Square Yard', 'Square Yard'), 3),
        SelectionOption('HECTARE', _t('Hectare', 'Hectare'), 4),
        SelectionOption('ACRE', _t('Acre', 'Acre'), 5),
        ),
        # source: data.spaces.spaceMeasureUnit
    ),
    FieldSpec(
        name='x_building_front',
        ttype='float',
        label=_t('Building Front', 'Building Front'),
        help=_t('building front facade in length measure unit (meter, inch, foot, yard, ...) Based on `spaces.spaceMeasureUnit`, so meters will be used as default if empty.', 'building front facade in length measure unit (meter, inch, foot, yard, ...) Based on `spaces.spaceMeasureUnit`, so meters will be used as default if empty.'),
        # source: data.spaces.buildingFront
    ),
    FieldSpec(
        name='x_overall_space',
        ttype='float',
        label=_t('Overall Space', 'Overall Space'),
        help=_t('total space of the property', 'total space of the property'),
        # source: data.spaces.overallSpace
    ),
    FieldSpec(
        name='x_usable_floor_space',
        ttype='float',
        label=_t('Usable Floor Space', 'Usable Floor Space'),
        help=_t('space that can be used, after deducting functional areas, stairs, etc. depending on the purpose', 'space that can be used, after deducting functional areas, stairs, etc. depending on the purpose'),
        # source: data.spaces.usableFloorSpace
    ),
    FieldSpec(
        name='x_space_max',
        ttype='float',
        label=_t('Space Max', 'Space Max'),
        help=_t('For a catalog house or a new built house or a program, the biggest property available, built or not yet built. If a property has different units/ spaces, this is the biggest space it has', 'For a catalog house or a new built house or a program, the biggest property available, built or not yet built. If a property has different units/ spaces, this is the biggest space it has'),
        # source: data.spaces.spaceMax
    ),
    FieldSpec(
        name='x_space_min',
        ttype='float',
        label=_t('Space Min', 'Space Min'),
        help=_t('For a catalog house or a new built house or a program, the smallest property available, built or not yet built. If a property has different units/ spaces, this is the smallest space it has', 'For a catalog house or a new built house or a program, the smallest property available, built or not yet built. If a property has different units/ spaces, this is the smallest space it has'),
        # source: data.spaces.spaceMin
    ),
    FieldSpec(
        name='x_plot_space',
        ttype='float',
        label=_t('Plot Space', 'Plot Space'),
        help=_t('space of the plot', 'space of the plot'),
        # source: data.spaces.plotSpace
    ),
    FieldSpec(
        name='x_plot_front',
        ttype='float',
        label=_t('Plot Front', 'Plot Front'),
        help=_t('plot front in length measure unit (meter, inch, foot, yard, ...) Based on `spaces.spaceMeasureUnit`, so meters will be used as default if empty.', 'plot front in length measure unit (meter, inch, foot, yard, ...) Based on `spaces.spaceMeasureUnit`, so meters will be used as default if empty.'),
        # source: data.spaces.plotFront
    ),
    FieldSpec(
        name='x_additional_space',
        ttype='float',
        label=_t('Additional Space', 'Additional Space'),
        help=_t('contains all cumulated additional space from outbuilding, extended or misc places.', 'contains all cumulated additional space from outbuilding, extended or misc places.'),
        # source: data.spaces.additionalSpace
    ),
    FieldSpec(
        name='x_kitchen_space',
        ttype='float',
        label=_t('Kitchen Space', 'Kitchen Space'),
        help=_t('space of the kitchen', 'space of the kitchen'),
        # source: data.spaces.kitchenSpace
    ),
    FieldSpec(
        name='x_living_space',
        ttype='float',
        label=_t('Living Space', 'Living Space'),
        help=_t('core space within a building in which people may live', 'core space within a building in which people may live'),
        # source: data.spaces.residential.livingSpace
    ),
    FieldSpec(
        name='x_living_room_space',
        ttype='float',
        label=_t('Living Room Space', 'Living Room Space'),
        help=_t('space of the livingroom in a house or apartment', 'space of the livingroom in a house or apartment'),
        # source: data.spaces.residential.livingRoomSpace
    ),
    FieldSpec(
        name='x_attic_space',
        ttype='float',
        label=_t('Attic Space', 'Attic Space'),
        help=_t('space directly under the roof of a building', 'space directly under the roof of a building'),
        # source: data.spaces.residential.atticSpace
    ),
    FieldSpec(
        name='x_balcony_space',
        ttype='float',
        label=_t('Balcony Space', 'Balcony Space'),
        help=_t('space of the balcony, seperated to terrace', 'space of the balcony, seperated to terrace'),
        # source: data.spaces.residential.balconySpace
    ),
    FieldSpec(
        name='x_cellar_space',
        ttype='float',
        label=_t('Cellar Space', 'Cellar Space'),
        help=_t('cellar space of the building or that belongs to the assigned unit, eg apartment, office', 'cellar space of the building or that belongs to the assigned unit, eg apartment, office'),
        # source: data.spaces.residential.cellarSpace
    ),
    FieldSpec(
        name='x_garden_space',
        ttype='float',
        label=_t('Garden Space', 'Garden Space'),
        help=_t('space of the garden', 'space of the garden'),
        # source: data.spaces.residential.gardenSpace
    ),
    FieldSpec(
        name='x_terrace_space',
        ttype='float',
        label=_t('Terrace Space', 'Terrace Space'),
        help=_t('space of the terrace, separated to balcony', 'space of the terrace, separated to balcony'),
        # source: data.spaces.residential.terraceSpace
    ),
    FieldSpec(
        name='x_bath_room_space',
        ttype='float',
        label=_t('Bath Room Space', 'Bath Room Space'),
        help=_t('space of the bathroom', 'space of the bathroom'),
        # source: data.spaces.residential.bathRoomSpace
    ),
    FieldSpec(
        name='x_shower_room_space',
        ttype='float',
        label=_t('Shower Room Space', 'Shower Room Space'),
        help=_t('space of the shower room', 'space of the shower room'),
        # source: data.spaces.residential.showerRoomSpace
    ),
    FieldSpec(
        name='x_dining_room_space',
        ttype='float',
        label=_t('Dining Room Space', 'Dining Room Space'),
        help=_t('space of the dining room', 'space of the dining room'),
        # source: data.spaces.residential.diningRoomSpace
    ),
    FieldSpec(
        name='x_max_divisible',
        ttype='float',
        label=_t('Max Divisible', 'Max Divisible'),
        help=_t('if a space can be divided, this is the maximum divisible space; not to be mixed up with the field spaceMax; not divisions and not a sum of divisions either.', 'if a space can be divided, this is the maximum divisible space; not to be mixed up with the field spaceMax; not divisions and not a sum of divisions either.'),
        # source: data.spaces.commercial.maxDivisible
    ),
    FieldSpec(
        name='x_min_divisible',
        ttype='float',
        label=_t('Min Divisible', 'Min Divisible'),
        help=_t('if a space can be divided, this is the minimum divisible space; not to be mixed up with the field spaceMin; not divisions and not a sum of divisions either.', 'if a space can be divided, this is the minimum divisible space; not to be mixed up with the field spaceMin; not divisions and not a sum of divisions either.'),
        # source: data.spaces.commercial.minDivisible
    ),
    FieldSpec(
        name='x_commercial_space',
        ttype='float',
        label=_t('Commercial Space', 'Commercial Space'),
        help=_t('amount of the space used for commercial purposes', 'amount of the space used for commercial purposes'),
        # source: data.spaces.commercial.commercialSpace
    ),
    FieldSpec(
        name='x_shop_space',
        ttype='float',
        label=_t('Shop Space', 'Shop Space'),
        help=_t('space of a shop or store', 'space of a shop or store'),
        # source: data.spaces.commercial.shopSpace
    ),
    FieldSpec(
        name='x_storage_space',
        ttype='float',
        label=_t('Storage Space', 'Storage Space'),
        help=_t('space of the storage area', 'space of the storage area'),
        # source: data.spaces.commercial.storageSpace
    ),
    FieldSpec(
        name='x_sell_space',
        ttype='float',
        label=_t('Sell Space', 'Sell Space'),
        help=_t('refers to the area used for sales, in the retail and service sectors', 'refers to the area used for sales, in the retail and service sectors'),
        # source: data.spaces.commercial.sellSpace
    ),
    FieldSpec(
        name='x_office_space',
        ttype='float',
        label=_t('Office Space', 'Office Space'),
        help=_t('space of the office', 'space of the office'),
        # source: data.spaces.commercial.officeSpace
    ),
    FieldSpec(
        name='x_office_part_space',
        ttype='float',
        label=_t('Office Part Space', 'Office Part Space'),
        help=_t('space of a single office unit in an office building with several units', 'space of a single office unit in an office building with several units'),
        # source: data.spaces.commercial.officePartSpace
    ),
    FieldSpec(
        name='x_management_space',
        ttype='float',
        label=_t('Management Space', 'Management Space'),
        help=_t('area used for administrative or management purposes', 'area used for administrative or management purposes'),
        # source: data.spaces.commercial.managementSpace
    ),
    FieldSpec(
        name='x_restaurant_space',
        ttype='float',
        label=_t('Restaurant Space', 'Restaurant Space'),
        help=_t('Amount of the restaurant space', 'Amount of the restaurant space'),
        # source: data.spaces.commercial.restaurantSpace
    ),
)

# ---- structure (82 fields) ----
DERIVED_STRUCTURE_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_attic',
        ttype='selection',
        label=_t('Attic', 'Attic'),
        help=_t('- CONVERTED: attic can be used as a living space. - PART_CONVERTED: attic is part converted, can be used as a living space but part of the space is still convertible - CONVERTIBLE: There is an attic, but work is required to use it as a living space.', '- CONVERTED: attic can be used as a living space. - PART_CONVERTED: attic is part converted, can be used as a living space but part of the space is still convertible - CONVERTIBLE: There is an attic, but work is required to use it as a living space.'),
        selection=(
        SelectionOption('CONVERTED', _t('Converted', 'Converted'), 0),
        SelectionOption('PART_CONVERTED', _t('Part Converted', 'Part Converted'), 1),
        SelectionOption('CONVERTIBLE', _t('Convertible', 'Convertible'), 2),
        ),
        # source: data.structure.building.attic
    ),
    FieldSpec(
        name='x_balcony_direction',
        ttype='selection',
        label=_t('Balcony Direction', 'Balcony Direction'),
        help=_t('cardinal and ordinal geographical directions', 'cardinal and ordinal geographical directions'),
        selection=(
        SelectionOption('NORTH', _t('North', 'North'), 0),
        SelectionOption('EAST', _t('East', 'East'), 1),
        SelectionOption('SOUTH', _t('South', 'South'), 2),
        SelectionOption('WEST', _t('West', 'West'), 3),
        SelectionOption('NORTH_EAST', _t('North East', 'North East'), 4),
        SelectionOption('SOUTH_EAST', _t('South East', 'South East'), 5),
        SelectionOption('NORTH_WEST', _t('North West', 'North West'), 6),
        SelectionOption('SOUTH_WEST', _t('South West', 'South West'), 7),
        SelectionOption('EAST_WEST', _t('East West', 'East West'), 8),
        SelectionOption('SOUTH_NORTH', _t('South North', 'South North'), 9),
        ),
        # source: data.structure.building.balconyDirection
    ),
    FieldSpec(
        name='x_garden_orientation',
        ttype='selection',
        label=_t('Garden Orientation', 'Garden Orientation'),
        help=_t('cardinal and ordinal geographical directions', 'cardinal and ordinal geographical directions'),
        selection=(
        SelectionOption('NORTH', _t('North', 'North'), 0),
        SelectionOption('EAST', _t('East', 'East'), 1),
        SelectionOption('SOUTH', _t('South', 'South'), 2),
        SelectionOption('WEST', _t('West', 'West'), 3),
        SelectionOption('NORTH_EAST', _t('North East', 'North East'), 4),
        SelectionOption('SOUTH_EAST', _t('South East', 'South East'), 5),
        SelectionOption('NORTH_WEST', _t('North West', 'North West'), 6),
        SelectionOption('SOUTH_WEST', _t('South West', 'South West'), 7),
        SelectionOption('EAST_WEST', _t('East West', 'East West'), 8),
        SelectionOption('SOUTH_NORTH', _t('South North', 'South North'), 9),
        ),
        # source: data.structure.building.gardenOrientation
    ),
    FieldSpec(
        name='x_barrier_free',
        ttype='selection',
        label=_t('Barrier Free', 'Barrier Free'),
        help=_t('property is accessible to people with mobility difficulties', 'property is accessible to people with mobility difficulties'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.barrierFree
    ),
    FieldSpec(
        name='x_shower',
        ttype='selection',
        label=_t('Shower', 'Shower'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        SelectionOption('ROMAN_SHOWER', _t('Roman Shower', 'Roman Shower'), 3),
        ),
        # source: data.structure.building.bath.shower
    ),
    FieldSpec(
        name='x_bathtub',
        ttype='selection',
        label=_t('Bathtub', 'Bathtub'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.bath.bathtub
    ),
    FieldSpec(
        name='x_bath_window',
        ttype='selection',
        label=_t('Bath Window', 'Bath Window'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.bath.window
    ),
    FieldSpec(
        name='x_bidet',
        ttype='selection',
        label=_t('Bidet', 'Bidet'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.bath.bidet
    ),
    FieldSpec(
        name='x_urinal',
        ttype='selection',
        label=_t('Urinal', 'Urinal'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.bath.urinal
    ),
    FieldSpec(
        name='x_guest_toilet',
        ttype='selection',
        label=_t('Guest Toilet', 'Guest Toilet'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.bath.guestToilet
    ),
    FieldSpec(
        name='x_separate_bath_and_toilet',
        ttype='selection',
        label=_t('Separate Bath And Toilet', 'Separate Bath And Toilet'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.bath.separateBathAndToilet
    ),
    FieldSpec(
        name='x_toilet',
        ttype='selection',
        label=_t('Toilet', 'Toilet'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.bath.toilet
    ),
    FieldSpec(
        name='x_bathroom_sink',
        ttype='selection',
        label=_t('Bathroom Sink', 'Bathroom Sink'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.bath.bathroomSink
    ),
    FieldSpec(
        name='x_cellar',
        ttype='selection',
        label=_t('Cellar', 'Cellar'),
        help=_t('cellar present', 'cellar present'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('PART', _t('Part', 'Part'), 2),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 3),
        ),
        # source: data.structure.building.cellar
    ),
    FieldSpec(
        name='x_person',
        ttype='selection',
        label=_t('Person', 'Person'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.elevator.person
    ),
    FieldSpec(
        name='x_freight',
        ttype='selection',
        label=_t('Freight', 'Freight'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.elevator.freight
    ),
    FieldSpec(
        name='x_built_in',
        ttype='boolean',
        label=_t('Built In', 'Built In'),
        help=_t('kitchen facilities and cabinets are fitted to the room providing a seamless, integrated look', 'kitchen facilities and cabinets are fitted to the room providing a seamless, integrated look'),
        # source: data.structure.building.kitchen.kitchenType.builtIn
    ),
    FieldSpec(
        name='x_kitchenette',
        ttype='boolean',
        label=_t('Kitchenette', 'Kitchenette'),
        help=_t('small cooking area usually with only basic facilities like refrigerator, hotplate and sink. Sometimes this is even hidden in a closet.', 'small cooking area usually with only basic facilities like refrigerator, hotplate and sink. Sometimes this is even hidden in a closet.'),
        # source: data.structure.building.kitchen.kitchenType.kitchenette
    ),
    FieldSpec(
        name='x_open',
        ttype='boolean',
        label=_t('Open', 'Open'),
        help=_t('an open-concept kitchen without walls separating it from the rest of the property.', 'an open-concept kitchen without walls separating it from the rest of the property.'),
        # source: data.structure.building.kitchen.kitchenType.open
    ),
    FieldSpec(
        name='x_separated',
        ttype='boolean',
        label=_t('Separated', 'Separated'),
        help=_t('the kitchen is a room of its own, separated from the rest of the living area.', 'the kitchen is a room of its own, separated from the rest of the living area.'),
        # source: data.structure.building.kitchen.kitchenType.separated
    ),
    FieldSpec(
        name='x_kitchen_equipment',
        ttype='selection',
        label=_t('Kitchen Equipment', 'Kitchen Equipment'),
        selection=(
        SelectionOption('NONE', _t('None', 'None'), 0),
        SelectionOption('STORAGE', _t('Storage', 'Storage'), 1),
        SelectionOption('FULLY_EQUIPPED', _t('Fully Equipped', 'Fully Equipped'), 2),
        ),
        # source: data.structure.building.kitchen.kitchenEquipment
    ),
    FieldSpec(
        name='x_pantry',
        ttype='selection',
        label=_t('Pantry', 'Pantry'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.kitchen.pantry
    ),
    FieldSpec(
        name='x_single_storey',
        ttype='selection',
        label=_t('Single Storey', 'Single Storey'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.kitchen.singleStorey
    ),
    FieldSpec(
        name='x_number_of_floors',
        ttype='integer',
        label=_t('Number Of Floors', 'Number Of Floors'),
        help=_t('total number of floors of a building. e.g. - a house is rented, it has 2 floors -> numberOfFloors: 2 - a 5 floor office building is sold -> numberOfFloors: 5', 'total number of floors of a building. e.g. - a house is rented, it has 2 floors -> numberOfFloors: 2 - a 5 floor office building is sold -> numberOfFloors: 5'),
        # source: data.structure.building.numberOfFloors
    ),
    FieldSpec(
        name='x_number_of_facades',
        ttype='integer',
        label=_t('Number Of Facades', 'Number Of Facades'),
        help=_t('number of exterior walls of the building separated from any adjacent building', 'number of exterior walls of the building separated from any adjacent building'),
        # source: data.structure.building.numberOfFacades
    ),
    FieldSpec(
        name='x_room_height',
        ttype='float',
        label=_t('Room Height', 'Room Height'),
        help=_t('room height in length measure unit (meter, inch, foot, ...) If there are several different buildings, put in the maximal room height Based on `spaces.spaceMeasureUnit`, so meters will be used as default if empty.', 'room height in length measure unit (meter, inch, foot, ...) If there are several different buildings, put in the maximal room height Based on `spaces.spaceMeasureUnit`, so meters will be used as default if empty.'),
        # source: data.structure.building.roomHeight
    ),
    FieldSpec(
        name='x_offered_floors',
        ttype='integer',
        label=_t('Offered Floors', 'Offered Floors'),
        help=_t('special case! refers to the number of floors explicitly offered on a property, e.g. a multistorey apartment can have 2 (duplex) or 3 (triplex) floors. ATTENTION! not to be confused with numberOfFloors!', 'special case! refers to the number of floors explicitly offered on a property, e.g. a multistorey apartment can have 2 (duplex) or 3 (triplex) floors. ATTENTION! not to be confused with numberOfFloors!'),
        # source: data.structure.building.offeredFloors
    ),
    FieldSpec(
        name='x_roof_style',
        ttype='selection',
        label=_t('Roof Style', 'Roof Style'),
        help=_t('Style of the roof', 'Style of the roof'),
        selection=(
        SelectionOption('HALF_HIPPED_ROOF', _t('Half Hipped Roof', 'Half Hipped Roof'), 0),
        SelectionOption('GAMBREL', _t('Gambrel', 'Gambrel'), 1),
        SelectionOption('MONO_PITCHED_ROOF', _t('Mono Pitched Roof', 'Mono Pitched Roof'), 2),
        SelectionOption('GABLE', _t('Gable', 'Gable'), 3),
        SelectionOption('HIP_ROOF', _t('Hip Roof', 'Hip Roof'), 4),
        SelectionOption('FLAT_ROOF', _t('Flat Roof', 'Flat Roof'), 5),
        SelectionOption('PYRAMIDAL_ROOF', _t('Pyramidal Roof', 'Pyramidal Roof'), 6),
        SelectionOption('OTHER', _t('Other', 'Other'), 7),
        ),
        # source: data.structure.building.roofStyle
    ),
    FieldSpec(
        name='x_location_in_building',
        ttype='selection',
        label=_t('Location In Building', 'Location In Building'),
        help=_t('Location of the apartment in the building - GROUNDFLOOR: apartment is located on the ground floor, so usually you do not have stairs - HALF_BASEMENT: apartment is located half below ground, so that it can still have windows to let in daylight - ROOF_STOREY: apartment is located directly under the roof with sloping ceiling', 'Location of the apartment in the building - GROUNDFLOOR: apartment is located on the ground floor, so usually you do not have stairs - HALF_BASEMENT: apartment is located half below ground, so that it can still have windows to let in daylight - ROOF_STOREY: apartment is located directly under the roof with sloping ceiling'),
        selection=(
        SelectionOption('GROUNDFLOOR', _t('Groundfloor', 'Groundfloor'), 0),
        SelectionOption('HALF_BASEMENT', _t('Half Basement', 'Half Basement'), 1),
        SelectionOption('ROOF_STOREY', _t('Roof Storey', 'Roof Storey'), 2),
        ),
        # source: data.structure.building.locationInBuilding
    ),
    FieldSpec(
        name='x_location_at_corner',
        ttype='selection',
        label=_t('Location At Corner', 'Location At Corner'),
        help=_t('the property is located at the corner of two streets', 'the property is located at the corner of two streets'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.locationAtCorner
    ),
    FieldSpec(
        name='x_calm',
        ttype='selection',
        label=_t('Calm', 'Calm'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.calm
    ),
    FieldSpec(
        name='x_courtyard_view',
        ttype='boolean',
        label=_t('Courtyard View', 'Courtyard View'),
        help=_t('with a view on the courtyard', 'with a view on the courtyard'),
        # source: data.structure.building.withView.courtyardView
    ),
    FieldSpec(
        name='x_lake_view',
        ttype='boolean',
        label=_t('Lake View', 'Lake View'),
        help=_t('with a view on the lake', 'with a view on the lake'),
        # source: data.structure.building.withView.lakeView
    ),
    FieldSpec(
        name='x_mountain_view',
        ttype='boolean',
        label=_t('Mountain View', 'Mountain View'),
        help=_t('with a view on the mountain', 'with a view on the mountain'),
        # source: data.structure.building.withView.mountainView
    ),
    FieldSpec(
        name='x_overlooking',
        ttype='boolean',
        label=_t('Overlooking', 'Overlooking'),
        help=_t('view when it cannot be seen from any other buildings', 'view when it cannot be seen from any other buildings'),
        # source: data.structure.building.withView.overlooking
    ),
    FieldSpec(
        name='x_sea_view',
        ttype='boolean',
        label=_t('Sea View', 'Sea View'),
        help=_t('with a view on the sea', 'with a view on the sea'),
        # source: data.structure.building.withView.seaView
    ),
    FieldSpec(
        name='x_ski_view',
        ttype='boolean',
        label=_t('Ski View', 'Ski View'),
        help=_t('with a view on the ski slope', 'with a view on the ski slope'),
        # source: data.structure.building.withView.skiView
    ),
    FieldSpec(
        name='x_luminous',
        ttype='selection',
        label=_t('Luminous', 'Luminous'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.luminous
    ),
    FieldSpec(
        name='x_bay_window',
        ttype='selection',
        label=_t('Bay Window', 'Bay Window'),
        help=_t('presence of a bay window', 'presence of a bay window'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.window.bayWindow
    ),
    FieldSpec(
        name='x_blinds',
        ttype='selection',
        label=_t('Blinds', 'Blinds'),
        help=_t('presence of blinds on the windows', 'presence of blinds on the windows'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        SelectionOption('ELECTRIC', _t('Electric', 'Electric'), 3),
        SelectionOption('MANUAL', _t('Manual', 'Manual'), 4),
        ),
        # source: data.structure.building.window.blinds
    ),
    FieldSpec(
        name='x_wooden_windows',
        ttype='selection',
        label=_t('Wooden Windows', 'Wooden Windows'),
        help=_t('presence of wooden windows', 'presence of wooden windows'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.window.windowMaterial.woodenWindows
    ),
    FieldSpec(
        name='x_aluminium_windows',
        ttype='selection',
        label=_t('Aluminium Windows', 'Aluminium Windows'),
        help=_t('presence of aluminium windows', 'presence of aluminium windows'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.window.windowMaterial.aluminiumWindows
    ),
    FieldSpec(
        name='x_muntin_windows',
        ttype='selection',
        label=_t('Muntin Windows', 'Muntin Windows'),
        help=_t('presence of muntin windows', 'presence of muntin windows'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.window.windowMaterial.muntinWindows
    ),
    FieldSpec(
        name='x_plastic_windows',
        ttype='selection',
        label=_t('Plastic Windows', 'Plastic Windows'),
        help=_t('presence of plastic windows', 'presence of plastic windows'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        ),
        # source: data.structure.building.window.windowMaterial.plasticWindows
    ),
    FieldSpec(
        name='x_insulated_glazing',
        ttype='selection',
        label=_t('Insulated Glazing', 'Insulated Glazing'),
        selection=(
        SelectionOption('YES', _t('Yes', 'Yes'), 0),
        SelectionOption('NO', _t('No', 'No'), 1),
        SelectionOption('NOT_APPLICABLE', _t('Not Applicable', 'Not Applicable'), 2),
        SelectionOption('SIMPLE', _t('Simple', 'Simple'), 3),
        SelectionOption('DOUBLE', _t('Double', 'Double'), 4),
        SelectionOption('TRIPLE', _t('Triple', 'Triple'), 5),
        ),
        # source: data.structure.building.window.windowMaterial.insulatedGlazing
    ),
    FieldSpec(
        name='x_shape',
        ttype='selection',
        label=_t('Shape', 'Shape'),
        help=_t('The shape of the house represents the external form of the house.', 'The shape of the house represents the external form of the house.'),
        selection=(
        SelectionOption('L_SHAPE', _t('L Shape', 'L Shape'), 0),
        SelectionOption('U_SHAPE', _t('U Shape', 'U Shape'), 1),
        SelectionOption('V_SHAPE', _t('V Shape', 'V Shape'), 2),
        SelectionOption('RECTANGULAR', _t('Rectangular', 'Rectangular'), 3),
        SelectionOption('SQUARE', _t('Square', 'Square'), 4),
        SelectionOption('OTHER', _t('Other', 'Other'), 5),
        ),
        # source: data.structure.building.shape
    ),
    FieldSpec(
        name='x_has_split_floor',
        ttype='boolean',
        label=_t('Has Split Floor', 'Has Split Floor'),
        help=_t('the property has at least one floor which level is between 2 other floors. This floor is not directly above or below these other floors. A "half floor" or a split floor.', 'the property has at least one floor which level is between 2 other floors. This floor is not directly above or below these other floors. A "half floor" or a split floor.'),
        # source: data.structure.building.hasSplitFloor
    ),
    FieldSpec(
        name='x_number_of_rooms',
        ttype='float',
        label=_t('Number Of Rooms', 'Number Of Rooms'),
        help=_t('number of rooms available in the property. Floating point numbers may also be used here, because half rooms are possible.', 'number of rooms available in the property. Floating point numbers may also be used here, because half rooms are possible.'),
        # source: data.structure.rooms.numberOfRooms
    ),
    FieldSpec(
        name='x_number_of_bed_rooms',
        ttype='integer',
        label=_t('Number Of Bed Rooms', 'Number Of Bed Rooms'),
        help=_t('number of bedrooms', 'number of bedrooms'),
        # source: data.structure.rooms.numberOfBedRooms
    ),
    FieldSpec(
        name='x_number_of_bath_rooms',
        ttype='integer',
        label=_t('Number Of Bath Rooms', 'Number Of Bath Rooms'),
        help=_t('number of bath and shower rooms. The separation is not obvious in some countries', 'number of bath and shower rooms. The separation is not obvious in some countries'),
        # source: data.structure.rooms.numberOfBathRooms
    ),
    FieldSpec(
        name='x_number_of_toilets',
        ttype='integer',
        label=_t('Number Of Toilets', 'Number Of Toilets'),
        help=_t('number of toilets as separated rooms', 'number of toilets as separated rooms'),
        # source: data.structure.rooms.numberOfToilets
    ),
    FieldSpec(
        name='x_number_of_powder_rooms',
        ttype='integer',
        label=_t('Number Of Powder Rooms', 'Number Of Powder Rooms'),
        help=_t('number of powder rooms available in the property. A powder room is smaller than a full bathroom and contains a sink and a toilet', 'number of powder rooms available in the property. A powder room is smaller than a full bathroom and contains a sink and a toilet'),
        # source: data.structure.rooms.numberOfPowderRooms
    ),
    FieldSpec(
        name='x_number_of_balconies',
        ttype='integer',
        label=_t('Number Of Balconies', 'Number Of Balconies'),
        help=_t('number of balconies', 'number of balconies'),
        # source: data.structure.rooms.numberOfBalconies
    ),
    FieldSpec(
        name='x_number_of_terraces',
        ttype='integer',
        label=_t('Number Of Terraces', 'Number Of Terraces'),
        help=_t('number of terraces (+ stalls for shops)', 'number of terraces (+ stalls for shops)'),
        # source: data.structure.rooms.numberOfTerraces
    ),
    FieldSpec(
        name='x_number_of_kitchens',
        ttype='integer',
        label=_t('Number Of Kitchens', 'Number Of Kitchens'),
        help=_t('number of kitchens', 'number of kitchens'),
        # source: data.structure.rooms.numberOfKitchens
    ),
    FieldSpec(
        name='x_rooms_number_of_units',
        ttype='integer',
        label=_t('Rooms Number Of Units', 'Rooms Number Of Units'),
        help=_t('number of units (residential or commercial)', 'number of units (residential or commercial)'),
        # source: data.structure.rooms.numberOfUnits
    ),
    FieldSpec(
        name='x_has_dining_room',
        ttype='boolean',
        label=_t('Has Dining Room', 'Has Dining Room'),
        help=_t('the property has a dining room, a room for eating meals', 'the property has a dining room, a room for eating meals'),
        # source: data.structure.rooms.hasDiningRoom
    ),
    FieldSpec(
        name='x_floor_load',
        ttype='integer',
        label=_t('Floor Load', 'Floor Load'),
        help=_t('maximal floor load for the property, expressed in Kg/m2', 'maximal floor load for the property, expressed in Kg/m2'),
        # source: data.structure.commercial.floorLoad
    ),
    FieldSpec(
        name='x_floor_load_upper_floors',
        ttype='float',
        label=_t('Floor Load Upper Floors', 'Floor Load Upper Floors'),
        help=_t('maximal floor load for the upper floors of the property, expressed in Kg/m2', 'maximal floor load for the upper floors of the property, expressed in Kg/m2'),
        # source: data.structure.commercial.floorLoadUpperFloors
    ),
    FieldSpec(
        name='x_hall_height',
        ttype='float',
        label=_t('Hall Height', 'Hall Height'),
        help=_t('hall height in length measure unit (meter, inch, foot, ...) If there are several different buildings, put in the maximal hall height Based on `spaces.spaceMeasureUnit`, so meters will be used as default if empty.', 'hall height in length measure unit (meter, inch, foot, ...) If there are several different buildings, put in the maximal hall height Based on `spaces.spaceMeasureUnit`, so meters will be used as default if empty.'),
        # source: data.structure.commercial.hallHeight
    ),
    FieldSpec(
        name='x_number_of_beds',
        ttype='integer',
        label=_t('Number Of Beds', 'Number Of Beds'),
        help=_t('number of beds in total (single and double beds included)', 'number of beds in total (single and double beds included)'),
        # source: data.structure.commercial.numberOfBeds
    ),
    FieldSpec(
        name='x_number_of_loading_docks',
        ttype='integer',
        label=_t('Number Of Loading Docks', 'Number Of Loading Docks'),
        help=_t('number of loading docks for trucks', 'number of loading docks for trucks'),
        # source: data.structure.commercial.numberOfLoadingDocks
    ),
    FieldSpec(
        name='x_number_of_desks',
        ttype='integer',
        label=_t('Number Of Desks', 'Number Of Desks'),
        # source: data.structure.commercial.numberOfDesks
    ),
    FieldSpec(
        name='x_number_of_meeting_rooms',
        ttype='integer',
        label=_t('Number Of Meeting Rooms', 'Number Of Meeting Rooms'),
        # source: data.structure.commercial.numberOfMeetingRooms
    ),
    FieldSpec(
        name='x_number_of_office_rooms',
        ttype='integer',
        label=_t('Number Of Office Rooms', 'Number Of Office Rooms'),
        # source: data.structure.commercial.numberOfOfficeRooms
    ),
    FieldSpec(
        name='x_window_front',
        ttype='float',
        label=_t('Window Front', 'Window Front'),
        help=_t('window front in length measure unit (meter, inch, foot, ...) Based on `spaces.spaceMeasureUnit`, so meters will be used as default if empty.', 'window front in length measure unit (meter, inch, foot, ...) Based on `spaces.spaceMeasureUnit`, so meters will be used as default if empty.'),
        # source: data.structure.commercial.windowFront
    ),
    FieldSpec(
        name='x_number_of_desks_max',
        ttype='integer',
        label=_t('Number Of Desks Max', 'Number Of Desks Max'),
        # source: data.structure.commercial.numberOfDesksMax
    ),
    FieldSpec(
        name='x_outside',
        ttype='integer',
        label=_t('Outside', 'Outside'),
        help=_t('number of parking spaces that are outside, not in a garage', 'number of parking spaces that are outside, not in a garage'),
        # source: data.structure.parkingLots.outside
    ),
    FieldSpec(
        name='x_street_parking',
        ttype='integer',
        label=_t('Street Parking', 'Street Parking'),
        help=_t('number of parking spaces along the street', 'number of parking spaces along the street'),
        # source: data.structure.parkingLots.streetParking
    ),
    FieldSpec(
        name='x_carport',
        ttype='integer',
        label=_t('Carport', 'Carport'),
        help=_t('number of carports (a shelter for vehicles that is open-sided and usually attached to a house)', 'number of carports (a shelter for vehicles that is open-sided and usually attached to a house)'),
        # source: data.structure.parkingLots.carport
    ),
    FieldSpec(
        name='x_parking_lots_garage',
        ttype='integer',
        label=_t('Parking Lots Garage', 'Parking Lots Garage'),
        help=_t('number of garages (building for parking one vehicle usually with a vertical rolling door)', 'number of garages (building for parking one vehicle usually with a vertical rolling door)'),
        # source: data.structure.parkingLots.garage
    ),
    FieldSpec(
        name='x_double_garage',
        ttype='integer',
        label=_t('Double Garage', 'Double Garage'),
        help=_t('number of doubleGarages (like a garage but for two vehicles)', 'number of doubleGarages (like a garage but for two vehicles)'),
        # source: data.structure.parkingLots.doubleGarage
    ),
    FieldSpec(
        name='x_duplex',
        ttype='integer',
        label=_t('Duplex', 'Duplex'),
        help=_t('number of duplex parking spaces (double parking on one parking space with a parking lift)', 'number of duplex parking spaces (double parking on one parking space with a parking lift)'),
        # source: data.structure.parkingLots.duplex
    ),
    FieldSpec(
        name='x_garage_area',
        ttype='integer',
        label=_t('Garage Area', 'Garage Area'),
        help=_t('number of garages in a garagesArea (with several garages only, no houses attached)', 'number of garages in a garagesArea (with several garages only, no houses attached)'),
        # source: data.structure.parkingLots.garageArea
    ),
    FieldSpec(
        name='x_parking_area',
        ttype='integer',
        label=_t('Parking Area', 'Parking Area'),
        help=_t('number of parking lots (in a confined area full of parking spaces)', 'number of parking lots (in a confined area full of parking spaces)'),
        # source: data.structure.parkingLots.parkingArea
    ),
    FieldSpec(
        name='x_car_park',
        ttype='integer',
        label=_t('Car Park', 'Car Park'),
        help=_t('number of parking spaces in a carPark (usually multistorey car park building)', 'number of parking spaces in a carPark (usually multistorey car park building)'),
        # source: data.structure.parkingLots.carPark
    ),
    FieldSpec(
        name='x_underground',
        ttype='integer',
        label=_t('Underground', 'Underground'),
        help=_t('number of parking spaces in a undergroundGarage (car park mainly below earth)', 'number of parking spaces in a undergroundGarage (car park mainly below earth)'),
        # source: data.structure.parkingLots.underground
    ),
    FieldSpec(
        name='x_boat_dock',
        ttype='integer',
        label=_t('Boat Dock', 'Boat Dock'),
        help=_t('number of parkings for a boat (a berth)', 'number of parkings for a boat (a berth)'),
        # source: data.structure.parkingLots.boatDock
    ),
    FieldSpec(
        name='x_maximal_capacity_of_persons',
        ttype='integer',
        label=_t('Maximal Capacity Of Persons', 'Maximal Capacity Of Persons'),
        # source: data.structure.countrySpecific.fr.maximalCapacityOfPersons
    ),
    FieldSpec(
        name='x_coefficient_occupation_des_sols',
        ttype='float',
        label=_t('Coefficient Occupation Des Sols', 'Coefficient Occupation Des Sols'),
        help=_t('COS, maximum occupancy rate of a property by buildings built on it', 'COS, maximum occupancy rate of a property by buildings built on it'),
        # source: data.structure.countrySpecific.fr.coefficientOccupationDesSols
    ),
    FieldSpec(
        name='x_coefficient_emprise_au_sol',
        ttype='float',
        label=_t('Coefficient Emprise Au Sol', 'Coefficient Emprise Au Sol'),
        help=_t('CES, actual occupancy rate of a property by the building(s) built on it', 'CES, actual occupancy rate of a property by the building(s) built on it'),
        # source: data.structure.countrySpecific.fr.coefficientEmpriseAuSol
    ),
    FieldSpec(
        name='x_height_under_door',
        ttype='float',
        label=_t('Height Under Door', 'Height Under Door'),
        help=_t('height between the floor and the bottom of a door, in cm', 'height between the floor and the bottom of a door, in cm'),
        # source: data.structure.countrySpecific.fr.heightUnderDoor
    ),
)

# ---- texts (34 fields) ----
DERIVED_TEXTS_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name='x_headline_en',
        ttype='text',
        label=_t('Headline En', 'Headline En'),
        # source: data.texts.headline.en
    ),
    FieldSpec(
        name='x_headline_fr',
        ttype='text',
        label=_t('Headline Fr', 'Headline Fr'),
        # source: data.texts.headline.fr
    ),
    FieldSpec(
        name='x_description_en',
        ttype='text',
        label=_t('Description En', 'Description En'),
        # source: data.texts.description.en
    ),
    FieldSpec(
        name='x_description_fr',
        ttype='text',
        label=_t('Description Fr', 'Description Fr'),
        # source: data.texts.description.fr
    ),
    FieldSpec(
        name='x_features_en',
        ttype='text',
        label=_t('Features En', 'Features En'),
        # source: data.texts.features.en
    ),
    FieldSpec(
        name='x_features_fr',
        ttype='text',
        label=_t('Features Fr', 'Features Fr'),
        # source: data.texts.features.fr
    ),
    FieldSpec(
        name='x_extended_information_en',
        ttype='text',
        label=_t('Extended Information En', 'Extended Information En'),
        # source: data.texts.extendedInformation.en
    ),
    FieldSpec(
        name='x_extended_information_fr',
        ttype='text',
        label=_t('Extended Information Fr', 'Extended Information Fr'),
        # source: data.texts.extendedInformation.fr
    ),
    FieldSpec(
        name='x_area_en',
        ttype='text',
        label=_t('Area En', 'Area En'),
        # source: data.texts.area.en
    ),
    FieldSpec(
        name='x_area_fr',
        ttype='text',
        label=_t('Area Fr', 'Area Fr'),
        # source: data.texts.area.fr
    ),
    FieldSpec(
        name='x_metro_en',
        ttype='text',
        label=_t('Metro En', 'Metro En'),
        # source: data.texts.transportation.metro.en
    ),
    FieldSpec(
        name='x_metro_fr',
        ttype='text',
        label=_t('Metro Fr', 'Metro Fr'),
        # source: data.texts.transportation.metro.fr
    ),
    FieldSpec(
        name='x_bus_en',
        ttype='text',
        label=_t('Bus En', 'Bus En'),
        # source: data.texts.transportation.bus.en
    ),
    FieldSpec(
        name='x_bus_fr',
        ttype='text',
        label=_t('Bus Fr', 'Bus Fr'),
        # source: data.texts.transportation.bus.fr
    ),
    FieldSpec(
        name='x_tramway_en',
        ttype='text',
        label=_t('Tramway En', 'Tramway En'),
        # source: data.texts.transportation.tramway.en
    ),
    FieldSpec(
        name='x_tramway_fr',
        ttype='text',
        label=_t('Tramway Fr', 'Tramway Fr'),
        # source: data.texts.transportation.tramway.fr
    ),
    FieldSpec(
        name='x_road_en',
        ttype='text',
        label=_t('Road En', 'Road En'),
        # source: data.texts.transportation.road.en
    ),
    FieldSpec(
        name='x_road_fr',
        ttype='text',
        label=_t('Road Fr', 'Road Fr'),
        # source: data.texts.transportation.road.fr
    ),
    FieldSpec(
        name='x_highway_en',
        ttype='text',
        label=_t('Highway En', 'Highway En'),
        # source: data.texts.transportation.highway.en
    ),
    FieldSpec(
        name='x_highway_fr',
        ttype='text',
        label=_t('Highway Fr', 'Highway Fr'),
        # source: data.texts.transportation.highway.fr
    ),
    FieldSpec(
        name='x_public_bike_system_en',
        ttype='text',
        label=_t('Public Bike System En', 'Public Bike System En'),
        # source: data.texts.transportation.publicBikeSystem.en
    ),
    FieldSpec(
        name='x_public_bike_system_fr',
        ttype='text',
        label=_t('Public Bike System Fr', 'Public Bike System Fr'),
        # source: data.texts.transportation.publicBikeSystem.fr
    ),
    FieldSpec(
        name='x_public_parking_en',
        ttype='text',
        label=_t('Public Parking En', 'Public Parking En'),
        # source: data.texts.transportation.publicParking.en
    ),
    FieldSpec(
        name='x_public_parking_fr',
        ttype='text',
        label=_t('Public Parking Fr', 'Public Parking Fr'),
        # source: data.texts.transportation.publicParking.fr
    ),
    FieldSpec(
        name='x_r_e_r_en',
        ttype='text',
        label=_t('R E R En', 'R E R En'),
        # source: data.texts.transportation.countrySpecific.fr.RER.en
    ),
    FieldSpec(
        name='x_r_e_r_fr',
        ttype='text',
        label=_t('R E R Fr', 'R E R Fr'),
        # source: data.texts.transportation.countrySpecific.fr.RER.fr
    ),
    FieldSpec(
        name='x_s_n_c_f_en',
        ttype='text',
        label=_t('S N C F En', 'S N C F En'),
        # source: data.texts.transportation.countrySpecific.fr.SNCF.en
    ),
    FieldSpec(
        name='x_s_n_c_f_fr',
        ttype='text',
        label=_t('S N C F Fr', 'S N C F Fr'),
        # source: data.texts.transportation.countrySpecific.fr.SNCF.fr
    ),
    FieldSpec(
        name='x_s_n_c_f_fret_en',
        ttype='text',
        label=_t('S N C F Fret En', 'S N C F Fret En'),
        # source: data.texts.transportation.countrySpecific.fr.SNCFFret.en
    ),
    FieldSpec(
        name='x_s_n_c_f_fret_fr',
        ttype='text',
        label=_t('S N C F Fret Fr', 'S N C F Fret Fr'),
        # source: data.texts.transportation.countrySpecific.fr.SNCFFret.fr
    ),
    FieldSpec(
        name='x_noctilien_en',
        ttype='text',
        label=_t('Noctilien En', 'Noctilien En'),
        # source: data.texts.transportation.countrySpecific.fr.noctilien.en
    ),
    FieldSpec(
        name='x_noctilien_fr',
        ttype='text',
        label=_t('Noctilien Fr', 'Noctilien Fr'),
        # source: data.texts.transportation.countrySpecific.fr.noctilien.fr
    ),
    FieldSpec(
        name='x_airport_shuttle_en',
        ttype='text',
        label=_t('Airport Shuttle En', 'Airport Shuttle En'),
        # source: data.texts.transportation.countrySpecific.fr.airportShuttle.en
    ),
    FieldSpec(
        name='x_airport_shuttle_fr',
        ttype='text',
        label=_t('Airport Shuttle Fr', 'Airport Shuttle Fr'),
        # source: data.texts.transportation.countrySpecific.fr.airportShuttle.fr
    ),
)

DERIVED_FIELD_GROUPS: tuple[tuple[dict, tuple[FieldSpec, ...]], ...] = (
    (_t('Building program', 'Programme immobilier'), DERIVED_BUILDING_PROPERTY_FIELDS),
    (_t('Conditions', 'Conditions'), DERIVED_CONDITIONS_FIELDS),
    (_t('Contact', 'Contact'), DERIVED_CONTACT_FIELDS),
    (_t('Country specifics', 'Spécificités pays'), DERIVED_COUNTRY_SPECIFIC_FIELDS),
    (_t('Distribution type', 'Type de distribution'), DERIVED_DISTRIBUTION_TYPE_FIELDS),
    (_t('Energy', 'Énergie'), DERIVED_ENERGY_FIELDS),
    (_t('Estate sub-type', 'Sous-type de bien'), DERIVED_ESTATE_SUB_TYPE_FIELDS),
    (_t('Estate type', 'Type de bien'), DERIVED_ESTATE_TYPE_FIELDS),
    (_t('Features', 'Caractéristiques'), DERIVED_FEATURES_FIELDS),
    (_t('Location', 'Localisation'), DERIVED_LOCATION_FIELDS),
    (_t('Management', 'Gestion'), DERIVED_MANAGEMENT_FIELDS),
    (_t('Meta Data', 'Meta Data'), DERIVED_META_DATA_FIELDS),
    (_t('Prices', 'Prix'), DERIVED_PRICES_FIELDS),
    (_t('Spaces', 'Surfaces'), DERIVED_SPACES_FIELDS),
    (_t('Structure', 'Structure'), DERIVED_STRUCTURE_FIELDS),
    (_t('Description', 'Description'), DERIVED_TEXTS_FIELDS),
)
