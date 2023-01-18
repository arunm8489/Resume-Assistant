# mapping variable contains the mapping between the source and target columns

def get_mapping():

    mapping = {
        
        
        'orders':[
        ("sf_order_id","int","sf_order_id","int"),
        ("source","string","source","string"),
        ("paid_at","timestamp","paid_at","timestamp"),
        ("currency_code","string","currency_code","string"),
        ("items_subtotal","decimal","items_subtotal","decimal"),
        ("tax_total","decimal","tax_total","decimal"),
        ("shipping_subtotal","decimal","shipping_subtotal","decimal"),
        ("order_total","decimal","order_total","decimal"),
        ("tax_type","string","tax_type","string"),
        ("tax_exemption_id","string","tax_exemption_id","string"),
        ("is_rush_shipping","boolean","is_rush_shipping","boolean"),
        ("freight_class","int","freight_class","int"),
        ("address1","string","address1","string"),
        ("address2","string","address2","string"),
        ("city","string","city","string"),
        ("state","string","state","string"),
        ("zipcode","string","zipcode","string"),
        ("country","string","country","string"),
        ("last_ledger_transaction_type","string","last_ledger_transaction_type","string"),
        ("last_ledger_transaction_at","timestamp","last_ledger_transaction_at","timestamp"),
        ("is_legacy","boolean","is_legacy","boolean"),
        ("checkout_bookmark","timestamp","checkout_bookmark","timestamp"),
        ("row_created_at","timestamp","row_created_at","timestamp"),
        ("row_updated_at","timestamp","row_updated_at","timestamp"),
        ("shipped_at","timestamp","shipped_at","timestamp"),
        ("tax_rate","decimal","tax_rate","decimal"),
        ("total_discount","decimal","total_discount","decimal"),
        
        # Mandatory Fields added by gluejob
        ("updatedby", "string", "updatedby", "string"),
        ("PipelineRunID", "string", "PipelineRunID", "string"),
        ("S3filename", "string", "S3filename", "string"),
        ("S3filepath", "string", "S3filepath", "string")],

        'order_items':[
        ("sf_order_item_id","int","sf_order_item_id","int"),
        ("sf_order_id","int","sf_order_id","int"),
        ("tax","decimal","tax","decimal"),
        ("price","decimal","price","decimal"),
        ("quantity","int","quantity","int"),
        ("row_created_at","timestamp","row_created_at","timestamp"),
        ("row_updated_at","timestamp","row_updated_at","timestamp"),
        ("discount","decimal","discount","decimal"),
        ("list_price","decimal","list_price","decimal"),
        ("tax_rate","decimal","tax_rate","decimal"),
        ("product_category","string","product_category","string"),
        ("original_sku","string","original_sku","string"),
        ("parent_sku","string","parent_sku","string"),
        
        # Mandatory Fields added by gluejob
        ("updatedby", "string", "updatedby", "string"),
        ("PipelineRunID", "string", "PipelineRunID", "string"),
        ("S3filename", "string", "S3filename", "string"),
        ("S3filepath", "string", "S3filepath", "string")
        
        
        
        ],

        
        'order_payment_transactions': [
        ("sf_order_id","int","sf_order_id","int"),
        ("payment_gateway_name","string","payment_gateway_name","string"),
        ("transaction_id","string","transaction_id","string"),
        ("transaction_type","string","transaction_type","string"),
        ("unreconciled_amount numeric","decimal","unreconciled_amount numeric","decimal"),
        ("row_created_at","timestamp","row_created_at","timestamp"),
        ("row_updated_at","timestamp","row_updated_at","timestamp"),
        
        # Mandatory Fields added by gluejob
        ("updatedby", "string", "updatedby", "string"),
        ("PipelineRunID", "string", "PipelineRunID", "string"),
        ("S3filename", "string", "S3filename", "string"),
        ("S3filepath", "string", "S3filepath", "string")],
        
        
        'internal_order_info': [
        ("sf_order_id","int","sf_order_id","int"),
        ("sf_user_id","int","sf_user_id","int"),
        ("email","string","email","string"),
        ("sf_purchased_order_id","int","sf_purchased_order_id","int"),
        ("requesting_user_id","int","requesting_user_id","int"),
        ("row_created_at","timestamp","row_created_at","timestamp"),
        ("row_updated_at","timestamp","row_updated_at","timestamp"), 
        ("order_type","string","order_type","string"),
        
        # Mandatory Fields added by gluejob
        ("updatedby", "string", "updatedby", "string"),
        ("PipelineRunID", "string", "PipelineRunID", "string"),
        ("S3filename", "string", "S3filename", "string"),
        ("S3filepath", "string", "S3filepath", "string")],

        'roostery_order_info' : [
         ("sf_order_id","int","sf_order_id","int"),
         ("sf_user_id","int","sf_user_id","int"),
         ("roostery_order_id","int","roostery_order_id","int"),
         ("roostery_user_id","int","roostery_user_id","int"),
         ("roostery_email","string","roostery_email","string"),
         ("sf_target_user_id","int","sf_target_user_id","int"),
         ("row_created_at","timestamp","row_created_at","timestamp"),
         ("row_updated_at","timestamp","row_updated_at","timestamp"),
         
        # Mandatory Fields added by gluejob
        ("updatedby", "string", "updatedby", "string"),
        ("PipelineRunID", "string", "PipelineRunID", "string"),
        ("S3filename", "string", "S3filename", "string"),
        ("S3filepath", "string", "S3filepath", "string")],
         
        
        'direct_order_info':[
        ("sf_order_id","int","sf_order_id","int"),
        ("sf_user_id","int","sf_user_id","int"),
        ("email","string","email","string"),
        ("sf_target_user_id","int","sf_target_user_id","int"),
        ("row_created_at","timestamp","row_created_at","timestamp"),
        ("row_updated_at","timestamp","row_updated_at","timestamp"),
         
        # Mandatory Fields added by gluejob
        ("updatedby", "string", "updatedby", "string"),
        ("PipelineRunID", "string", "PipelineRunID", "string"),
        ("S3filename", "string", "S3filename", "string"),
        ("S3filepath", "string", "S3filepath", "string")],
        
        'distro_order_info':[
            
        ("sf_order_id","int","sf_order_id","int"),    
        ("marketplace_order_id","string","marketplace_order_id","string"),
        ("marketplace","string","marketplace","string"),
        ("customer_id","string","customer_id","string"),
        ("shop_platform","string","shop_platform","string"),
        ("shop_code","string","shop_code","string"),
        ("shop_group","string","shop_group","string"),
        ("customer_email","string", "customer_email","string"),  
        ("sf_target_user_id","int","sf_target_user_id","int"),
        ("row_created_at","timestamp","row_created_at","timestamp"),
        ("row_updated_at","timestamp","row_updated_at","timestamp"),
         
        # Mandatory Fields added by gluejob
        ("updatedby", "string", "updatedby", "string"),
        ("PipelineRunID", "string", "PipelineRunID", "string"),
        ("S3filename", "string", "S3filename", "string"),
        ("S3filepath", "string", "S3filepath", "string")]
        
        
        }
    
    return mapping
        

if __name__=="__main__":
    x = get_mapping()
    print(x)