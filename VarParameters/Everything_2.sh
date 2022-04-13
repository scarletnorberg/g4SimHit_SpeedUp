declare -A parameters

# declare the list of values
RusRo_vals=(0.1 0.01 0.001 0.0001 0.00001)
RusRo_energy=(5.0 10.0 40.0 60.0 100.0 120.0)

# assigning array elements a specific value list
#parameters[RusRoEcalGamma]=RusRo_vals[@]
for varnames in $@; do
        if [ "$varnames" = "RusRoGammaEnergyLimit" ]; then
                parameters[RusRoGammaEnergyLimit]=RusRo_energy[@]
        elif [ "$varnames" = "RusRoEcalGamma" ]; then
                parameters[RusRoEcalGamma]=RusRo_vals[@]
        elif [ "$varnames" = "RusRoHcalGamma" ]; then
                parameters[RusRoHcalGamma]=RusRo_vals[@]
        elif [ "$varnames" = "RusRoMuonIronGamma" ]; then
                parameters[RusRoMuonIronGamma]=RusRo_vals[@]
        elif [ "$varnames" = "RusRoNeutronEnergyLimit" ]; then
                parameters[RusRoNeutronEnergyLimit]=RusRo_energy[@]
        elif [ "$varnames" = "RusRoEcalNeutron" ]; then
                parameters[RusRoEcalNeutron]=RusRo_vals[@]
        elif [ "$varnames" = "RusRoHcalNeutron" ]; then
                parameters[RusRoHcalNeutron]=RusRo_vals[@]
        elif [ "$varnames" = "RusRoMuonIronNeutron" ]; then
                parameters[RusRoMuonIronNeutron]=RusRo_vals[@]

        fi
done
