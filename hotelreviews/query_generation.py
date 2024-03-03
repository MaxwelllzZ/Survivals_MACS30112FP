"""
This file is to generate querylink for scraping and
merging hotel revenue/reviews data.
"""
def querylink(data):
    """
    generate querylink
    input:
        data(df): hotel revenue data
    output:
        data(df): hotel revenue data with querylink
    """
    data["Location_Address"] = data["Location_Address"].str.strip()
    data["Location_Name"] = data["Location_Name"].str.strip()
    data["Location_City"] = data["Location_City"].str.strip()
    data["hotelQuery"] = data[["Location_Name", "Location_City",
                                "Location_Address"]].agg('+'.join, axis=1)
    data["hotelQuery"] = data["hotelQuery"].str.replace(" ", "+")
    return data