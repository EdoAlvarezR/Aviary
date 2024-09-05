from aviary.variable_info.variables import Aircraft


def mass_defaults(prob):
    """
    This function is not used. Should we keep this file?
    """
    prob.model.set_input_defaults(
        Aircraft.Strut.ATTACHMENT_LOCATION, val=0, units='unitless')
    prob.model.set_input_defaults(
        Aircraft.VerticalTail.ASPECT_RATIO, val=1.67, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.HorizontalTail.TAPER_RATIO, val=0.352, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Engine.WING_LOCATIONS, val=0.35, units="unitless")
    prob.model.set_input_defaults(
        Aircraft.Fuselage.PRESSURE_DIFFERENTIAL, val=7.5, units="psi"
    )
    prob.model.set_input_defaults(
        Aircraft.Fuel.WING_FUEL_FRACTION, 0.6, units="unitless")
    prob.model.set_input_defaults(
        Aircraft.VerticalTail.TAPER_RATIO, val=0.801, units="unitless"
    )

    prob.model.set_input_defaults(
        Aircraft.HorizontalTail.VOLUME_COEFFICIENT, val=1.189, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.VerticalTail.VOLUME_COEFFICIENT, 0.145, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Fuselage.DELTA_DIAMETER, 4.5, units="ft"
    )
    prob.model.set_input_defaults(
        Aircraft.Fuselage.PILOT_COMPARTMENT_LENGTH, 9.5, units="ft"
    )
    prob.model.set_input_defaults(
        Aircraft.Fuselage.NOSE_FINENESS, 1, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Fuselage.TAIL_FINENESS, 3, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.VerticalTail.MOMENT_RATIO, 2.362, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.HorizontalTail.ASPECT_RATIO, val=4.75, units="unitless"
    )
    prob.model.set_input_defaults(Aircraft.Engine.REFERENCE_DIAMETER, 5.8, units="ft")
    prob.model.set_input_defaults(
        Aircraft.Nacelle.CORE_DIAMETER_RATIO, 1.25, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Nacelle.FINENESS, 2, units="unitless")

    prob.model.set_input_defaults(
        Aircraft.Design.MAX_STRUCTURAL_SPEED,
        val=402.5,
        units="mi/h",
    )
    prob.model.set_input_defaults(
        Aircraft.Design.LIFT_CURVE_SLOPE,
        val=7.1765,
        units="unitless",
    )

    prob.model.set_input_defaults(
        Aircraft.CrewPayload.CARGO_MASS, val=10040, units="lbm"
    )
    prob.model.set_input_defaults(
        Aircraft.HorizontalTail.MASS_COEFFICIENT,
        val=0.232,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.LandingGear.TAIL_HOOK_MASS_SCALER, val=1,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.VerticalTail.MASS_COEFFICIENT,
        val=0.289,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.HorizontalTail.THICKNESS_TO_CHORD,
        val=0.12,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.VerticalTail.THICKNESS_TO_CHORD,
        val=0.12,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.Wing.HIGH_LIFT_MASS_COEFFICIENT,
        val=2.66,
        units="lbm/ft**2",
    )
    prob.model.set_input_defaults(
        Aircraft.Wing.SURFACE_CONTROL_MASS_COEFFICIENT,
        val=0.95,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.Design.COCKPIT_CONTROL_MASS_COEFFICIENT,
        val=16.5,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.Controls.STABILITY_AUGMENTATION_SYSTEM_MASS, val=0, units="lbm"
    )
    prob.model.set_input_defaults(
        Aircraft.Controls.COCKPIT_CONTROL_MASS_SCALER, val=1, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Wing.SURFACE_CONTROL_MASS_SCALER, val=1, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Controls.STABILITY_AUGMENTATION_SYSTEM_MASS_SCALER, val=1, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Controls.TOTAL_MASS,
        val=0,
        units="lbm",
    )
    prob.model.set_input_defaults(
        Aircraft.LandingGear.MASS_COEFFICIENT, val=0.04,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.LandingGear.MAIN_GEAR_MASS_COEFFICIENT, val=0.85,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Nacelle.CLEARANCE_RATIO,
        val=0.2,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.Engine.MASS_SPECIFIC,
        val=0.21366,
        units="lbm/lbf",
    )
    prob.model.set_input_defaults(
        Aircraft.Nacelle.MASS_SPECIFIC,
        val=3,
        units="lbm/ft**2",
    )
    prob.model.set_input_defaults(
        Aircraft.Engine.PYLON_FACTOR, val=1.25,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Engine.ADDITIONAL_MASS_FRACTION, val=0.14,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Engine.MASS_SCALER, val=1, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Propulsion.MISC_MASS_SCALER, val=1, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.LandingGear.MAIN_GEAR_LOCATION,
        val=0.15,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.Instruments.MASS_COEFFICIENT,
        val=0.0736,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.Hydraulics.FLIGHT_CONTROL_MASS_COEFFICIENT,
        val=0.112,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.Hydraulics.GEAR_MASS_COEFFICIENT,
        val=0.14,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.Avionics.MASS,
        val=1959.0,
        units="lbm",
    )
    prob.model.set_input_defaults(
        Aircraft.AirConditioning.MASS_COEFFICIENT,
        val=1.65,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.AntiIcing.MASS,
        val=551.0,
        units="lbm",
    )
    prob.model.set_input_defaults(
        Aircraft.Furnishings.MASS,
        val=11192.0,
        units="lbm",
    )
    prob.model.set_input_defaults(
        Aircraft.CrewPayload.PASSENGER_SERVICE_MASS_PER_PASSENGER,
        val=5.0,
        units="lbm",
    )
    prob.model.set_input_defaults(
        Aircraft.CrewPayload.WATER_MASS_PER_OCCUPANT,
        val=3.0,
        units="lbm",
    )
    prob.model.set_input_defaults(
        Aircraft.Design.EMERGENCY_EQUIPMENT_MASS,
        val=50.0,
        units="lbm",
    )
    prob.model.set_input_defaults(
        Aircraft.CrewPayload.CATERING_ITEMS_MASS_PER_PASSENGER,
        val=7.6,
        units="lbm",
    )
    prob.model.set_input_defaults(
        Aircraft.Fuel.UNUSABLE_FUEL_MASS_COEFFICIENT,
        val=12.0,
        units="unitless",
    )

    prob.model.set_input_defaults(
        Aircraft.Wing.MASS_COEFFICIENT,
        val=102.5,
        units="unitless",
    )

    prob.model.set_input_defaults(
        Aircraft.Fuselage.MASS_COEFFICIENT,
        val=128,
        units="unitless",
    )
    prob.model.set_input_defaults(
        "static_analysis.total_mass.fuel_mass.fus_and_struct.pylon_len",
        val=0,
        units='ft',
    )
    prob.model.set_input_defaults(
        "static_analysis.total_mass.fuel_mass.fus_and_struct.MAT", val=0,
        units='lbm'
    )
    prob.model.set_input_defaults(
        Aircraft.Wing.MASS_SCALER, val=1,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.HorizontalTail.MASS_SCALER, val=1,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.VerticalTail.MASS_SCALER, val=1,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Fuselage.MASS_SCALER, val=1,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.LandingGear.TOTAL_MASS_SCALER, val=1,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Engine.POD_MASS_SCALER, val=1,
        units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Design.STRUCTURAL_MASS_INCREMENT,
        val=0,
        units='lbm',
    )
    prob.model.set_input_defaults(
        Aircraft.Fuel.FUEL_SYSTEM_MASS_SCALER, val=1, units="unitless"
    )
    prob.model.set_input_defaults(
        Aircraft.Fuel.FUEL_SYSTEM_MASS_COEFFICIENT,
        val=0.041,
        units="unitless",
    )
    prob.model.set_input_defaults(
        Aircraft.Fuel.DENSITY, val=6.687, units="lbm/galUS"
    )
    prob.model.set_input_defaults(
        Aircraft.VerticalTail.SWEEP,
        val=25.0,
        units="deg",
    )

    return prob
