📊 NYC Airbnb Market Analysis Dashboard (Tableau)

An interactive, enterprise-grade business intelligence dashboard designed to decode the pricing dynamics, distributions, and host configurations of the New York City Airbnb marketplace.
This repository houses the data pipeline documentation, underlying schema design, and analytical framework for the live dashboard hosted permanently on Tableau Public.

🎯 Summary & Core Intent

Navigating NYC's short-term rental market presents distinct challenges for prospective hosts, property managers, and urban researchers due to vast structural variances across the five boroughs. The true intent of this dashboard is to transform millions of rows of granular, messy reservation and property metrics into high-impact, scannable market intelligence.

On the other side of that coin is the perspective of prospective travellers planning to visit NYC, looking for a place to stay for their tenure. Using the interactive traveller's dashbord, users can find the perfect place to stay based on their individual needs filtering by borough, price, or no. of bedrooms of the listing.

Data Normalization & Modeling:

The Core Fact Table (Listings): Contains localized spatial metrics (latitude/longitude), exact price points, room configurations, and baseline review scores.
The Temporal Table (Calendar): Tracks forward-looking availability, daily price variations, and minimum-night mandates over a rolling 365-day horizon.
The Dimension Table (Hosts): Isolate single-listing casual hosts from highly active, multi-listing institutional property managers.

🚀 Key Dashboard Features & Design Choices

📍 1. Geospatial Density Map
The Build: A dual-axis map layering filled borough boundaries with a granular density heat map of individual listings.
Design Choice: Implemented localized zoom actions, allowing users to select a borough (e.g., Brooklyn) and automatically filter down to micro-neighborhood clusters (e.g., Williamsburg, Bushwick).

💰 2. Outlier-Resistant Price Distributions
The Build: Dynamic box plots and whisker charts combined with localized median trend lines.
Design Choice: Because less than 2% of luxury listings skew standard averages upward, the dashboard utilizes Median Price per Night as the central benchmark, giving users an honest view of the baseline market.

🏢 3. Room Type Matrix & Regulatory Impact Tracker
The Build: A cross-tabulated breakdown of Entire Homes vs. Private Rooms, paired with a calculated field tracking minimum stay mandates.
Design Choice: Built an interactive filter specifically isolating listings with a Minimum Nights >= 30 flag to evaluate how hosts are adapting to NYC's strict local short-term housing regulations.
