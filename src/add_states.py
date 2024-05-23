from db import DBO
import json

class RegionAggregatedStats(DBO):
    
    def calculate_region_stats(self):
        region_stats = {}
        select_statement = """
        SELECT r.name AS region_name, COUNT(c.id) AS number_countries, SUM(c.population) AS total_population
        FROM country c
        JOIN region r ON c.region_id = r.id
        GROUP BY r.name;
        """
        self.cursor.execute(select_statement)
        for row in self.cursor.fetchall():
            region_name, number_countries, total_population = row
            region_stats[region_name] = {
                "name": region_name,
                "number_countries": number_countries,
                "total_population": total_population
            }
    
        return region_stats

    def run(self):
        output = {"regions": list(self.calculate_region_stats().values())}
        json_output = json.dumps(output, indent=4)
        print(json_output)

if __name__ == "__main__":
    RegionAggregatedStats().run()
