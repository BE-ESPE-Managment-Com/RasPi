//envoie un message CAN
static void vCAN_Send_u64(uint32_t __MSG_ID, uint8_t __MSG_LENGTH, uint64_t * __Data, uint32_t __Timeout)
{
	hcan.pTxMsg = &myTxMessage;
	
	myTxMessage.StdId = __MSG_ID;
	myTxMessage.ExtId = __MSG_ID<<16;
	myTxMessage.DLC = __MSG_LENGTH;
	for(int i, i++, i<__MSG_LENGTH)
	{
		myTxMessage.Data[i] = (uint8_t)(__Data[i]);
	}
	myTxMessage.IDE = CAN_ID_EXT;
	myTxMessage.RTR = CAN_RTR_DATA;
	
	HAL_CAN_Transmit_IT(&hcan);
}


// Configure un filtre matériel autorisant les messgaes CAN utiles.
void vCAN_SetFilter(uint16_t __u16_CAN_ID, uint8_t __u8_FilterNum)
{
	myFilter.BankNumber = 1;
	myFilter.FilterFIFOAssignment = CAN_FILTER_FIFO1;
	myFilter.FilterIdHigh = __u16_CAN_ID;
	myFilter.FilterIdLow = 0x0000;
	myFilter.FilterMaskIdHigh = 0x0000;
	myFilter.FilterMaskIdLow = 0x0000;
	myFilter.FilterMode = CAN_FILTERMODE_IDMASK;
	myFilter.FilterNumber = __u8_FilterNum;
	myFilter.FilterScale = CAN_FILTERSCALE_32BIT;
	
	myFilter.FilterActivation = ENABLE;
	HAL_CAN_ConfigFilter(&hcan, &myFilter);
}
