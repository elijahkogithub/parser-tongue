from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Testing for COVID-19 with Opentrons',
    'author': 'Elijah Ko, Open Cell <elijah.ko@network.rca.ac.uk / hkk18@ic.ac.uk>',
    'description': 'Population-scale testing for COVID-19',
    'apiLevel': '2.0'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '1')
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat', '2')
    tuberack1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '3')
    tuberack2 = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '6')
    block = protocol.load_labware('opentrons_24_aluminumblock_nest_2ml_snapcap', '10')

    # pipettes
    left_pipette = protocol.load_instrument(
         'p300_single', 'right', tip_racks=[tiprack])

    # commands
    left_pipette.pick_up_tip()
    left_pipette.aspirate(200, plate['A1'])
    left_pipette.dispense(20, plate['B2'])
    left_pipette.dispense(20, plate['B3'])
    left_pipette.dispense(20, plate['B4'])
    left_pipette.dispense(20, plate['B5'])
    left_pipette.dispense(20, plate['B6'])
    left_pipette.dispense(20, plate['B7'])
    left_pipette.dispense(20, plate['B8'])
    left_pipette.dispense(20, plate['B9'])
    left_pipette.dispense(20, plate['B10'])
    left_pipette.drop_tip()

    left_pipette.pick_up_tip()
    left_pipette.aspirate(200, block['A1'])
    left_pipette.dispense(20, plate['D2'])
    left_pipette.dispense(20, plate['D3'])
    left_pipette.dispense(20, plate['D4'])
    left_pipette.dispense(20, plate['D5'])
    left_pipette.dispense(20, plate['D6'])
    left_pipette.dispense(20, plate['D7'])
    left_pipette.dispense(20, plate['D8'])
    left_pipette.dispense(20, plate['D9'])
    left_pipette.dispense(20, plate['D10'])
    left_pipette.drop_tip()

    left_pipette.pick_up_tip()
    left_pipette.aspirate(200, plate['A2'])
    left_pipette.dispense(20, plate['F2'])
    left_pipette.dispense(20, plate['F3'])
    left_pipette.dispense(20, plate['F4'])
    left_pipette.dispense(20, plate['F5'])
    left_pipette.dispense(20, plate['F6'])
    left_pipette.dispense(20, plate['F7'])
    left_pipette.dispense(20, plate['F8'])
    left_pipette.dispense(20, plate['F9'])
    left_pipette.dispense(20, plate['F10'])
    left_pipette.drop_tip()
