import csv

def get_location_from_zip(zip_code):
    """
    Search the local 'uszips.csv' file for the given ZIP code.
    Returns a dictionary with 'latitude' and 'longitude'.
    """
    try:
        with open("uszips.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["zip"] == zip_code:
                    lat = float(row["lat"])
                    lon = float(row["lng"])
                    return {"latitude": lat, "longitude": lon}
        print("❌ Could not find ZIP code in the file.")
        return None
    except FileNotFoundError:
        print("🚨 Error: File 'uszips.csv' not found.")
        return None

def calculate_tilt(lat, season):
    """Calculate optimal tilt angle based on season."""
    if season == "Winter":
        return round(lat + 15, 2)
    elif season == "Spring/Fall":
        return round(lat, 2)
    elif season == "Summer":
        return round(lat - 15, 2)
    else:
        return None

def main():
    print("🌟 Solar Panel Tilt Angle Calculator")
    zip_code = input("Enter your ZIP code: ")

    # Get location data
    location = get_location_from_zip(zip_code)
    if not location:
        return

    lat = location["latitude"]
    print(f"\n📍 Latitude: {lat}°")

    # Calculate tilt angles for each season
    seasons = ["Winter", "Spring/Fall", "Summer"]
    results = {season: calculate_tilt(lat, season) for season in seasons}

    # Display results
    print("\n📐 Recommended Tilt Angles (Degrees):")
    for season, angle in results.items():
        print(f"- {season}: {angle}°")

if __name__ == "__main__":
    main()
