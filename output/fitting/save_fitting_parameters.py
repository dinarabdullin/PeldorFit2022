from supplement.definitions import const


def save_fitting_parameters(parameters_indices, optimized_parameters_values, fixed_parameters_values, parameters_errors, filepath):    
    ''' Saves optimized and fixed fitting parameters ''' 
    file = open(filepath, 'w')
    file.write("{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}\n".format('Parameter', 'No. spin pair', 'No. component', 'Optimized', 'Value', 'Precision'))
    for parameter_name in const['fitting_parameters_names']:
        parameter_indices = parameters_indices[parameter_name]
        for i in range(len(parameter_indices)):
            for j in range(len(parameter_indices[i])):
                file.write('{:<20}'.format(const['fitting_parameters_names_and_units'][parameter_name]))
                file.write('{:<15}'.format(i+1))
                file.write('{:<15}'.format(j+1))
                parameter_object = parameter_indices[i][j]
                if parameter_object.optimize:
                    file.write('{:<15}'.format('yes'))
                else:
                    file.write('{:<15}'.format('no'))
                if parameter_object.optimize:
                    variable_value = optimized_parameters_values[parameter_object.index] / const['fitting_parameters_scales'][parameter_name]
                    file.write('{:<15.4}'.format(variable_value))
                else:
                    variable_value = fixed_parameters_values[parameter_object.index]  / const['fitting_parameters_scales'][parameter_name]
                    file.write('{:<15.4}'.format(variable_value))
                if parameter_object.optimize:
                    if parameters_errors != []:
                        if not np.isnan(parameters_errors[parameter_object.index]):
                            variable_error = parameters_errors[parameter_object.index] / const['fitting_parameters_scales'][parameter_name]
                            file.write('{:<15.4}'.format(variable_error))
                        else:
                            file.write('{:<15}'.format('nan'))
                    else:
                        file.write('{:<15}'.format('nan'))
                else:
                    file.write('{:<15}'.format('nan'))    
                file.write('\n') 
    file.close()