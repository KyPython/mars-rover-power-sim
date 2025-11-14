import numpy as np
import matplotlib.pyplot as plt

class MarsRoverPowerSim:
    def __init__(self):
        # Constants
        self.rtg_power = 110  # Watts
        self.battery_capacity = 42  # Amp-hours @ 28V = 1176 Wh
        self.max_battery_Wh = self.battery_capacity * 28
        self.sol_duration = 24.6  # hours
        # Temperature affects heater needs
        self.mars_temp_profile = self.generate_temp_profile()

    def generate_temp_profile(self):
        """Mars temperature over one sol."""
        hours = np.linspace(0, 24.6, 100)
        # Sinusoidal approximation
        temp = -80 + 60 * np.sin(2*np.pi*hours/24.6 - np.pi/2)
        return temp

    def calculate_heater_power(self, temp):
        """Heaters needed to keep electronics warm."""
        if temp < -40:
            return 50  # Watts
        elif temp < -20:
            return 30
        elif temp < 0:
            return 15
        else:
            return 5

    def simulate_sol(self):
        """Simulate full day of operations."""
        hours = np.linspace(0, 24.6, 100)
        power_usage = []
        battery_charge = []
        current_battery = self.max_battery_Wh * 0.75 
        for i, hour in enumerate(hours):
            temp = self.mars_temp_profile[i]
            computer = 5
            heater = self.calculate_heater_power(temp)
            baseline = computer + heater
            if 8 < hour < 18:
                science = 60
            else:
                science = 0
            if 6 < hour < 7 or 20 < hour < 21:
                comm = 15
            else:
                comm = 5
            total_power = baseline + science + comm
            time_step = self.sol_duration / len(hours)
            net_energy = (self.rtg_power - total_power) * time_step
            current_battery += net_energy
            current_battery = np.clip(current_battery, 0, self.max_battery_Wh)
            power_usage.append(total_power)
            battery_charge.append(current_battery)
        return hours, power_usage, battery_charge

    def visualize(self):
        hours, power_usage, battery_charge = self.simulate_sol()
        battery_percent = [c / self.max_battery_Wh * 100 for c in battery_charge]
        fig, ax1 = plt.subplots(figsize=(12, 6))
        ax1.plot(hours, power_usage, label='Total Power Load (W)', color='red')
        ax1.hlines(self.rtg_power, 0, self.sol_duration, label=f'MMRTG Power (C = {self.rtg_power}W)', color='gray', linestyle='--')
        power_np = np.array(power_usage)
        fill_color = np.where(power_np > self.rtg_power, 'lightcoral', 'lightgreen')
        ax1.fill_between(hours, power_np, self.rtg_power, where=(power_np > self.rtg_power), interpolate=True, color=fill_color[power_np > self.rtg_power], alpha=0.3, label='Battery Discharge')
        ax1.fill_between(hours, power_np, self.rtg_power, where=(power_np < self.rtg_power), interpolate=True, color=fill_color[power_np < self.rtg_power], alpha=0.3, label='Battery Charge')
        ax1.set_xlabel('Time (Hours into Sol)')
        ax1.set_ylabel('Power (Watts)', color='red')
        ax1.tick_params(axis='y', labelcolor='red')
        ax1.set_title('Perseverance Rover Power and Battery State Over One Sol (24.6 hours)')
        ax1.grid(True)
        ax1.legend(loc='upper left')
        ax2 = ax1.twinx()
        ax2.plot(hours, battery_percent, label='Battery State of Charge (%)', color='blue', linestyle='-')
        ax2.set_ylabel('Battery State of Charge (%)', color='blue')
        ax2.tick_params(axis='y', labelcolor='blue')
        ax2.set_ylim(0, 100)
        ax2.legend(loc='upper right')
        plt.show()

if __name__ == "__main__":
    sim = MarsRoverPowerSim()
    sim.visualize()
