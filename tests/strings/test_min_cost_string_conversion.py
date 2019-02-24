from strings.min_cost_string_conversion import assemble_transformation,compute_transform_tables

class TestMinCostStringConversion:
    
    def test_min_cost_string_conversion(self):
        _, operations = compute_transform_tables('Python', 'Algorithms', -1, 1, 2, 2)
    
        m = len(operations)
        n = len(operations[0])
        sequence = assemble_transformation(operations, m-1, n-1)
    
        string = list('Python')
        i = 0
        cost = 0
        
        with open('min_cost.txt', 'w') as file:
            for op in sequence:
                    
                if op[0] == 'C':
                    file.write('%-16s' % 'Copy %c' % op[1])
                    file.write('\t\t\t' + ''.join(string))
                    file.write('\r\n')
                    
                    cost -= 1
                elif op[0] == 'R':
                    string[i] = op[2]
    
                    file.write('%-16s' % ('Replace %c' % op[1] + ' with ' + str(op[2])))
                    file.write('\t\t' + ''.join(string))
                    file.write('\r\n')
                    
                    cost += 1
                elif op[0] == 'D':
                    string.pop(i)
    
                    file.write('%-16s' % 'Delete %c' % op[1])
                    file.write('\t\t\t' + ''.join(string))
                    file.write('\r\n')
                    
                    cost += 2
                else:
                    string.insert(i, op[1])
    
                    file.write('%-16s' % 'Insert %c' % op[1])
                    file.write('\t\t\t' + ''.join(string))
                    file.write('\r\n')
                    
                    cost += 2
    
                i += 1
            assert cost == 10